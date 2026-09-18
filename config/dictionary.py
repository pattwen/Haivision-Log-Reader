# 中文的映射
METRIC_NAME_MAP = {
    'bandwidth': '带宽占用',
    'bitrate': '码率',
    'cpu_usage': 'CPU利用率',
    'latency': '延迟数据',
    'mem_usage': '内存使用率',
    'numpackets': '传输的数据包数量',
    'packetloss': 'TS丢包数量',
    'retransmitrate': '重传包数',
    'roundtriptime': 'rtt',
    'signalLosses': '信源丢失',
    'srtBufferLevel': '实时Buffer',
    'srtEstimatedBandwidth': '估测的可用带宽',
    'srtNumLostPackets': '丢包数量',
    'srtNumSkippedPackets': '弃包数量',
    'vmem_usage': '虚拟内存使用率',
    'srtDroppedPackets': 'srt丢弃包数量(疑似弃用)',
    'srtMaxBandwidth': '最大带宽占用',
    'srtPacketLossRate': 'srt丢包率'
}

# 英文的映射
METRIC_NAME_MAP_EN = {
    'bandwidth': 'Bandwidth Usage',
    'bitrate': 'Bitrate',
    'cpu_usage': 'CPU Utilization',
    'latency': 'Latency',
    'mem_usage': 'Memory Usage',
    'numpackets': 'Number of Transmitted Packets',
    'packetloss': 'TS Packet Loss',
    'retransmitrate': 'Retransmitted Packets',
    'roundtriptime': 'RTT',
    'signalLosses': 'Signal Loss',
    'srtBufferLevel': 'Real-time Buffer Level',
    'srtEstimatedBandwidth': 'Estimated Available Bandwidth',
    'srtNumLostPackets': 'Number of Lost Packets',
    'srtNumSkippedPackets': 'Number of Skipped Packets',
    'vmem_usage': 'Virtual Memory Usage',
    'srtDroppedPackets': 'SRT Dropped Packets (Suspected Deprecated)',
    'srtMaxBandwidth': 'Maximum Bandwidth Usage',
    'srtPacketLossRate': 'SRT Packet Loss Rate'
}

def get_chinese_name(key: str) -> str:
    return METRIC_NAME_MAP.get(key, key)

def get_english_name(key: str) -> str:
    return METRIC_NAME_MAP_EN.get(key, key)
