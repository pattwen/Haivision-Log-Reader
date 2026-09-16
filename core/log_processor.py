import os
import json
import csv
from urllib.parse import unquote
import numpy as np
import pandas as pd
import plotly.graph_objects as go

from config.sys_config import STORAGE_UPLOADS_DIR, STORAGE_RESULTS_DIR
from config.dictionary import get_chinese_name
from utils.time_utils import (
    timestamp_to_target_datetime, 
    get_timezone_info, 
    format_to_iso, 
    UTC_TZ, 
    DEFAULT_TIMEZONE_KEY
)
from core.i18n_utils import t as lag


def parse_stream_info(tags: dict) -> dict:
    if not tags:
        return {
            "direction": "未知",
            "stream_name": "",
            "ip": "",
            "port": "",
            "display_label": "",
            "file_tag": ""
        }
    
    raw_input = tags.get("input", "")
    raw_output = tags.get("output", "") or tags.get("preset_label", "")
    
    input_name = unquote(str(raw_input)) if raw_input else ""
    output_name = unquote(str(raw_output)) if raw_output else ""
    
    ip = str(tags.get("address", "")).strip()
    port = str(tags.get("port", "")).strip()

    if input_name:
        direction = "输入"
        stream_name = input_name
    elif output_name:
        direction = "输出"
        stream_name = output_name
    else:
        direction = "未知"
        stream_name = ""

    formatted_ip = f"ipaddr-{ip.replace('.', '_')}" if ip else ""
    formatted_port = f"port-{port}" if port else ""

    file_tag_parts = []
    if stream_name:
        file_tag_parts.append(f"{direction}{stream_name}")
    elif direction != "未知":
        file_tag_parts.append(direction)

    if formatted_ip:
        file_tag_parts.append(formatted_ip)
    if formatted_port:
        file_tag_parts.append(formatted_port)

    file_tag = "_".join(file_tag_parts)

    ip_port_ui = f"{ip}:{port}" if ip and port else (ip or port)
    ui_parts = []
    if stream_name:
        ui_parts.append(f"{direction}:{stream_name}")
    if ip_port_ui:
        ui_parts.append(ip_port_ui)
    display_label = " | ".join(ui_parts)

    return {
        "direction": direction,
        "stream_name": stream_name,
        "ip": ip,
        "port": port,
        "display_label": display_label,
        "file_tag": file_tag
    }


def min_max_downsample(x_times, y_values, max_points=6000):
    total_points = len(x_times)
    if total_points <= max_points:
        return x_times, y_values

    x_arr = np.array(x_times)
    y_arr = np.array(y_values)

    num_buckets = max_points // 2
    chunks_y = np.array_split(y_arr, num_buckets)

    selected_indices = []
    current_index = 0

    for chunk_y in chunks_y:
        if len(chunk_y) > 0:
            min_idx = current_index + np.argmin(chunk_y)
            max_idx = current_index + np.argmax(chunk_y)
            selected_indices.extend([min_idx, max_idx])
            current_index += len(chunk_y)

    unique_indices = sorted(list(set(selected_indices)))
    return x_arr[unique_indices].tolist(), y_arr[unique_indices].tolist()


def detect_srt_anomalies(x_times, y_values, metric_name=""):
    anomaly_x = []
    anomaly_y = []
    
    if not y_values:
        return anomaly_x, anomaly_y

    y_arr = np.array(y_values, dtype=float)
    
    if "loss" in metric_name.lower() or "丢包" in metric_name:
        anom_indices = np.where(y_arr > 0)[0]
    else:
        mean = np.mean(y_arr)
        std = np.std(y_arr)
        if std > 0:
            anom_indices = np.where(y_arr > mean + 3 * std)[0]
        else:
            anom_indices = []

    for idx in anom_indices:
        anomaly_x.append(x_times[idx])
        anomaly_y.append(y_values[idx])

    return anomaly_x, anomaly_y

def process_log_task(task_id: str, target_tz_key: str = DEFAULT_TIMEZONE_KEY) -> bool:
    input_dir = os.path.join(STORAGE_UPLOADS_DIR, task_id)
    output_dir = os.path.join(STORAGE_RESULTS_DIR, task_id)
    json_path = os.path.join(input_dir, "log.json")
    
    if not os.path.exists(json_path):
        raise FileNotFoundError(f"{lag('consolelog.Original_file_notfound')} {json_path}")
        
    os.makedirs(output_dir, exist_ok=True)

    tz_info = get_timezone_info(target_tz_key)
    local_time_header = tz_info["header_name"]

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    print(f"[{task_id}] Starting to process logs with timezone: {target_tz_key} ({local_time_header})")
    print(f"[{task_id}] Total number of top-level data items: {len(data)}")

    index = 0
    items = data if isinstance(data, list) else [data]

    for item in items:
        results = item.get("results", [])
        if not results:
            continue

        for res in results:
            series_list = res.get("series", [])
            for series_data in series_list:
                en_jsonName = series_data.get("name", "unknown")
                zh_metric_name = get_chinese_name(en_jsonName) or en_jsonName
                
                tags = series_data.get("tags", {})
                stream_info = parse_stream_info(tags)
                
                file_tag = stream_info["file_tag"]
                display_label = stream_info["display_label"]
                
                full_display_name = f"{zh_metric_name} ({display_label})" if display_label else zh_metric_name
                file_prefix_name = f"{zh_metric_name}_{file_tag}" if file_tag else zh_metric_name
                
                safe_file_prefix = "".join(
                    c for c in file_prefix_name 
                    if c.isalnum() or c in ('_', '-')
                ).rstrip()

                csv_filename = os.path.join(output_dir, f"{safe_file_prefix}-{index}.csv")
                html_filename = os.path.join(output_dir, f"{safe_file_prefix}-{index}.html")
                index += 1

                values = series_data.get("values", [])
                x_times = []
                y_values = []

                with open(csv_filename, 'w', newline='', encoding='utf-8-sig') as csvfile:
                    datawriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    datawriter.writerow([local_time_header, "UTC Time", "Direction", "Stream Name", "IP Address", "Port ", full_display_name])

                    for value in values:
                        if not value or len(value) < 2:
                            continue

                        ms_timestamp = value[0]
                        val = value[1]

                        dt_target = timestamp_to_target_datetime(ms_timestamp, target_tz_key)
                        dt_utc = dt_target.astimezone(UTC_TZ)

                        datawriter.writerow([
                            format_to_iso(dt_target), 
                            format_to_iso(dt_utc),
                            stream_info["direction"],
                            stream_info["stream_name"],
                            stream_info["ip"],
                            stream_info["port"],
                            val
                        ])

                        x_times.append(dt_target.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
                        
                        if isinstance(val, (int, float)):
                            y_values.append(val)
                        elif isinstance(val, str) and val.replace('.', '', 1).isdigit():
                            y_values.append(float(val) if '.' in val else int(val))
                        else:
                            y_values.append(0)

                fig = go.Figure()

                opt_x, opt_y = min_max_downsample(x_times, y_values, max_points=6000)

                fig.add_trace(go.Scatter(
                    x=opt_x, 
                    y=opt_y, 
                    mode='lines', 
                    name=full_display_name,
                    line=dict(width=1.5, color='#2563eb'),
                    hovertemplate=f'<b>{local_time_header}</b>: %{{x}}<br><b>Value</b>: %{{y}}<extra></extra>'
                ))

                anom_x, anom_y = detect_srt_anomalies(x_times, y_values, zh_metric_name)
                if anom_x:
                    fig.add_trace(go.Scatter(
                        x=anom_x,
                        y=anom_y,
                        mode='markers',
                        name='Warning',
                        marker=dict(color='#ef4444', size=7, symbol='x-open'),
                        hovertemplate='<b>[Warning]</b><br>Time: %{x}<br>Value: <b>%{y}</b><extra></extra>'
                    ))
                fig.update_layout(
                    title=dict(
                        text=f"SRT Data Trend Charts: <b>{full_display_name}</b>",
                        font=dict(size=16, color="#0f172a"),
                        x=0.0,
                        y=0.98,
                        xanchor='left',
                        yanchor='top'
                    ),
                    hovermode="x unified",
                    hoverlabel=dict(
                        bgcolor="rgba(255, 255, 255, 0.95)",
                        font_size=12,
                        font_family="Monospace"
                    ),
                    xaxis=dict(
                        title=dict(text=local_time_header, font=dict(size=12, color="#475569")),
                        tickformat="%m-%d\n%H:%M:%S",
                        showgrid=True,
                        gridcolor="#f1f5f9",
                        showspikes=True,
                        spikemode="across",
                        spikesnap="cursor",
                        spikedash="dash",
                        spikethickness=1,
                        spikecolor="#94a3b8",
                        rangeselector=dict(
                            buttons=list([
                                dict(count=5, label="5min", step="minute", stepmode="backward"),
                                dict(count=30, label="30min", step="minute", stepmode="backward"),
                                dict(count=1, label="1hour", step="hour", stepmode="backward"),
                                dict(count=6, label="6hour", step="hour", stepmode="backward"),
                                dict(count=12, label="12hour", step="hour", stepmode="backward"),
                                dict(step="all", label="All")
                            ]),
                            x=1.0,               
                            y=1.12,              
                            xanchor="right",     
                            yanchor="bottom",
                            bgcolor="#ffffff",
                            activecolor="#2563eb",
                            bordercolor="#e2e8f0",
                            borderwidth=1,
                            font=dict(size=11, color="#334155")
                        ),
                        rangeslider=dict(
                            visible=True,
                            thickness=0.07,
                            bgcolor="#f8fafc",                  
                            bordercolor="#cbd5e1",              
                            borderwidth=1,
                            yaxis=dict(rangemode="auto")
                        ),
                        type="date"
                    ),
                    yaxis=dict(
                        title=dict(text=zh_metric_name, font=dict(size=12, color="#475569")),
                        showgrid=True,
                        gridcolor="#f1f5f9",
                        zeroline=True,
                        zerolinecolor="#cbd5e1",
                        fixedrange=False
                    ),
                    height=720,
                    autosize=True,
                    margin=dict(l=60, r=40, t=110, b=40),
                    template="plotly_white"
                )

                fig.write_html(
                    html_filename, 
                    include_plotlyjs='cdn', 
                    full_html=False,
                    config={
                        'scrollZoom': True,
                        'displayModeBar': True,
                        'displaylogo': False,
                        'responsive': True
                    }
                )

                print(f"[{task_id}] {lag('consolelog.export_html_done')} {safe_file_prefix}")
    print(f"[{task_id}] {lag('consolelog.analysis_done')}")
    return True