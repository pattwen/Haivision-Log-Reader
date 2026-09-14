import os
from flask import Blueprint, render_template, send_from_directory, abort

from db.task_manager import get_task_by_id
from config.sys_config import STORAGE_RESULTS_DIR
from core.i18n_utils import t as lag

report_bp = Blueprint('report', __name__)

@report_bp.route('/report/<task_id>', methods=['GET'])
def view_report(task_id):
    task = get_task_by_id(task_id)
    if not task:
        return lag('htmlreturn.mission_notfound'), 404

    if task.status != 'Completed':
        return f"[{task.status}] {lag('htmlreturn.mission_state_wrong')}", 400

    result_dir = os.path.join(STORAGE_RESULTS_DIR, task_id)
    if not os.path.exists(result_dir):
        return lag('htmlreturn.logfile_deleted'), 404

    all_files = os.listdir(result_dir)
    chart_htmls = [f for f in all_files if f.endswith('.html')]
    csv_files = [f for f in all_files if f.endswith('.csv')]

    chart_htmls.sort()
    csv_files.sort()

    return render_template(
        'report.html',
        task=task,
        chart_htmls=chart_htmls,
        csv_files=csv_files
    )

@report_bp.route('/report/<task_id>/files/<filename>', methods=['GET'])
def get_report_file(task_id, filename):
    result_dir = os.path.join(STORAGE_RESULTS_DIR, task_id)
    if not os.path.exists(os.path.join(result_dir, filename)):
        abort(404)
    return send_from_directory(result_dir, filename)