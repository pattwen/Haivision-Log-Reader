from datetime import datetime
import pytz

UTC_TZ = pytz.utc

TIMEZONE_CONFIG = {
    "UTC": {
        "tz": pytz.utc,
        "header_name": "UTC Time",
        "header_name_cn": "UTC 时间",
        "header_name_local": "UTC Time",
        "utc_offset": "UTC+0",
        "display_name_zh": "UTC 时间",
        "display_name_en": "UTC Time"
    },
    "Europe/London": {
        "tz": pytz.timezone("Europe/London"),
        "header_name": "London Time",
        "header_name_cn": "伦敦时间",
        "header_name_local": "London Time",
        "utc_offset": "UTC+0",
        "display_name_zh": "伦敦时间 (UTC+0)",
        "display_name_en": "London Time (UTC+0)"
    },
    "Etc/GMT+12": {
        "tz": pytz.timezone("Etc/GMT+12"),
        "header_name": "Baker Island Time",
        "header_name_cn": "贝克岛时间",
        "header_name_local": "Baker Island Time",
        "utc_offset": "UTC-12",
        "display_name_zh": "贝克岛时间 (西十二区 UTC-12)",
        "display_name_en": "Baker Island Time (UTC-12)"
    },
    "Pacific/Pago_Pago": {
        "tz": pytz.timezone("Pacific/Pago_Pago"),
        "header_name": "Samoa Standard Time",
        "header_name_cn": "美属萨摩亚时间",
        "header_name_local": "Samoa Standard Time",
        "utc_offset": "UTC-11",
        "display_name_zh": "美属萨摩亚时间 (西十一区 UTC-11)",
        "display_name_en": "Samoa Time (UTC-11)"
    },
    "Pacific/Honolulu": {
        "tz": pytz.timezone("Pacific/Honolulu"),
        "header_name": "Hawaii Time",
        "header_name_cn": "夏威夷时间",
        "header_name_local": "Hawaii Time",
        "utc_offset": "UTC-10",
        "display_name_zh": "夏威夷时间 (西十区 UTC-10)",
        "display_name_en": "Hawaii Time (UTC-10)"
    },
    "America/Anchorage": {
        "tz": pytz.timezone("America/Anchorage"),
        "header_name": "Alaska Time",
        "header_name_cn": "阿拉斯加时间",
        "header_name_local": "Alaska Time",
        "utc_offset": "UTC-9",
        "display_name_zh": "阿拉斯加时间 (西九区 UTC-9)",
        "display_name_en": "Alaska Time (UTC-9)"
    },
    "America/Los_Angeles": {
        "tz": pytz.timezone("America/Los_Angeles"),
        "header_name": "Pacific Time",
        "header_name_cn": "太平洋时间",
        "header_name_local": "Pacific Time",
        "utc_offset": "UTC-8",
        "display_name_zh": "太平洋时间 / 洛杉矶 (西八区 UTC-8)",
        "display_name_en": "Pacific Time / Los Angeles (UTC-8)"
    },
    "America/Denver": {
        "tz": pytz.timezone("America/Denver"),
        "header_name": "Mountain Time",
        "header_name_cn": "山地时间",
        "header_name_local": "Mountain Time",
        "utc_offset": "UTC-7",
        "display_name_zh": "山地时间 / 丹佛 (西七区 UTC-7)",
        "display_name_en": "Mountain Time / Denver (UTC-7)"
    },
    "America/Chicago": {
        "tz": pytz.timezone("America/Chicago"),
        "header_name": "Central Time",
        "header_name_cn": "中部时间",
        "header_name_local": "Central Time",
        "utc_offset": "UTC-6",
        "display_name_zh": "中部时间 / 芝加哥 (西六区 UTC-6)",
        "display_name_en": "Central Time / Chicago (UTC-6)"
    },
    "America/New_York": {
        "tz": pytz.timezone("America/New_York"),
        "header_name": "Eastern Time",
        "header_name_cn": "东部时间",
        "header_name_local": "Eastern Time",
        "utc_offset": "UTC-5",
        "display_name_zh": "东部时间 / 纽约 (西五区 UTC-5)",
        "display_name_en": "Eastern Time / New York (UTC-5)"
    },
    "America/Santiago": {
        "tz": pytz.timezone("America/Santiago"),
        "header_name": "Santiago Time",
        "header_name_cn": "圣地亚哥时间",
        "header_name_local": "Hora de Santiago",
        "utc_offset": "UTC-4",
        "display_name_zh": "圣地亚哥时间 / 智利 (西四区 UTC-4)",
        "display_name_en": "Santiago Time / Chile (UTC-4)"
    },
    "America/Argentina/Buenos_Aires": {
        "tz": pytz.timezone("America/Argentina/Buenos_Aires"),
        "header_name": "Buenos Aires Time",
        "header_name_cn": "布宜诺斯艾利斯时间",
        "header_name_local": "Hora de Buenos Aires",
        "utc_offset": "UTC-3",
        "display_name_zh": "布宜诺斯艾利斯时间 (西三区 UTC-3)",
        "display_name_en": "Buenos Aires Time (UTC-3)"
    },
    "America/Noronha": {
        "tz": pytz.timezone("America/Noronha"),
        "header_name": "Noronha Time",
        "header_name_cn": "费尔南多时间",
        "header_name_local": "Horário de Noronha",
        "utc_offset": "UTC-2",
        "display_name_zh": "费尔南多时间 / 巴西 (西二区 UTC-2)",
        "display_name_en": "Noronha Time / Brazil (UTC-2)"
    },
    "Atlantic/Cape_Verde": {
        "tz": pytz.timezone("Atlantic/Cape_Verde"),
        "header_name": "Cape Verde Time",
        "header_name_cn": "佛得角时间",
        "header_name_local": "Hora de Cabo Verde",
        "utc_offset": "UTC-1",
        "display_name_zh": "佛得角时间 (西一区 UTC-1)",
        "display_name_en": "Cape Verde Time (UTC-1)"
    },
    "Europe/Paris": {
        "tz": pytz.timezone("Europe/Paris"),
        "header_name": "Paris Time",
        "header_name_cn": "巴黎时间 ",
        "header_name_local": "Heure de Paris",
        "utc_offset": "UTC+1",
        "display_name_zh": "巴黎时间 / 中欧时间 (东一区 UTC+1)",
        "display_name_en": "Paris Time / CET (UTC+1)"
    },
    "Europe/Kyiv": {
        "tz": pytz.timezone("Europe/Kyiv"),
        "header_name": "Kyiv Time",
        "header_name_cn": "基辅时间",
        "header_name_local": "Київський час",
        "utc_offset": "UTC+2",
        "display_name_zh": "基辅时间 / 东欧时间 (东二区 UTC+2)",
        "display_name_en": "Kyiv Time / EET (UTC+2)"
    },
    "Europe/Moscow": {
        "tz": pytz.timezone("Europe/Moscow"),
        "header_name": "Moscow Time",
        "header_name_cn": "莫斯科时间",
        "header_name_local": "Московское время",
        "utc_offset": "UTC+3",
        "display_name_zh": "莫斯科时间 (东三区 UTC+3)",
        "display_name_en": "Moscow Time (UTC+3)"
    },
    "Asia/Dubai": {
        "tz": pytz.timezone("Asia/Dubai"),
        "header_name": "Dubai Time",
        "header_name_cn": "迪拜时间",
        "header_name_local": "توقيت دبي",
        "utc_offset": "UTC+4",
        "display_name_zh": "迪拜时间 (东四区 UTC+4)",
        "display_name_en": "Dubai Time (UTC+4)"
    },
    "Asia/Karachi": {
        "tz": pytz.timezone("Asia/Karachi"),
        "header_name": "Karachi Time",
        "header_name_cn": "巴基斯坦时间",
        "header_name_local": "Pakistan Standard Time",
        "utc_offset": "UTC+5",
        "display_name_zh": "卡拉奇 / 巴基斯坦时间 (东五区 UTC+5)",
        "display_name_en": "Karachi Time / Pakistan (UTC+5)"
    },
    "Asia/Dhaka": {
        "tz": pytz.timezone("Asia/Dhaka"),
        "header_name": "Dhaka Time ",
        "header_name_cn": "孟加拉国时间",
        "header_name_local": "বাংলাদেশ সময়",
        "utc_offset": "UTC+6",
        "display_name_zh": "达卡 / 孟加拉国时间 (东六区 UTC+6)",
        "display_name_en": "Dhaka Time / Bangladesh (UTC+6)"
    },
    "Asia/Bangkok": {
        "tz": pytz.timezone("Asia/Bangkok"),
        "header_name": "Bangkok Time",
        "header_name_cn": "泰国时间",
        "header_name_local": "เวลาไทย",
        "utc_offset": "UTC+7",
        "display_name_zh": "曼谷 / 泰国时间 (东七区 UTC+7)",
        "display_name_en": "Bangkok Time / Thailand (UTC+7)"
    },
    "Asia/Shanghai": {
        "tz": pytz.timezone("Asia/Shanghai"),
        "header_name": "Beijing Time",
        "header_name_cn": "北京时间",
        "header_name_local": "北京时间",
        "utc_offset": "UTC+8",
        "display_name_zh": "北京时间 (东八区 UTC+8)",
        "display_name_en": "Beijing Time (UTC+8)"
    },
    "Asia/Tokyo": {
        "tz": pytz.timezone("Asia/Tokyo"),
        "header_name": "Tokyo Time",
        "header_name_cn": "东京时间",
        "header_name_local": "东京時間",
        "utc_offset": "UTC+9",
        "display_name_zh": "东京时间 (东九区 UTC+9)",
        "display_name_en": "Tokyo Time (UTC+9)"
    },
    "Australia/Sydney": {
        "tz": pytz.timezone("Australia/Sydney"),
        "header_name": "Sydney Time",
        "header_name_cn": "悉尼时间",
        "header_name_local": "Sydney Time",
        "utc_offset": "UTC+10",
        "display_name_zh": "悉尼时间 (东十区 UTC+10)",
        "display_name_en": "Sydney Time (UTC+10)"
    },
    "Pacific/Noumea": {
        "tz": pytz.timezone("Pacific/Noumea"),
        "header_name": "Noumea Time",
        "header_name_cn": "努美阿时间",
        "header_name_local": "Heure de Nouméa",
        "utc_offset": "UTC+11",
        "display_name_zh": "努美阿时间 (东十一区 UTC+11)",
        "display_name_en": "Noumea Time (UTC+11)"
    },
    "Pacific/Auckland": {
        "tz": pytz.timezone("Pacific/Auckland"),
        "header_name": "New Zealand Time",
        "header_name_cn": "新西兰时间",
        "header_name_local": "New Zealand Time",
        "utc_offset": "UTC+12",
        "display_name_zh": "奥克兰 / 新西兰时间 (东十二区 UTC+12)",
        "display_name_en": "Auckland / NZ Time (UTC+12)"
    },
    "Pacific/Fiji": {
        "tz": pytz.timezone("Pacific/Fiji"),
        "header_name": "Fiji Time",
        "header_name_cn": "斐济时间",
        "header_name_local": "Fiji Time",
        "utc_offset": "UTC+12",
        "display_name_zh": "斐济时间 (东十二区 UTC+12)",
        "display_name_en": "Fiji Time (UTC+12)"
    },
    "Asia/Tehran": {
        "tz": pytz.timezone("Asia/Tehran"),
        "header_name": "Tehran Time",
        "header_name_cn": "伊朗时间",
        "header_name_local": "توقيت تهران",
        "utc_offset": "UTC+3:30",
        "display_name_zh": "德黑兰 / 伊朗时间 (UTC+3:30)",
        "display_name_en": "Tehran Time / Iran (UTC+3:30)"
    },
    "Asia/Kolkata": {
        "tz": pytz.timezone("Asia/Kolkata"),
        "header_name": "Indian Standard Time",
        "header_name_cn": "印度标准时间",
        "header_name_local": "Indian Standard Time",
        "utc_offset": "UTC+5:30",
        "display_name_zh": "印度标准时间 (UTC+5:30)",
        "display_name_en": "Indian Standard Time (UTC+5:30)"
    }
}

DEFAULT_TIMEZONE_KEY = "Asia/Shanghai"

def get_timezone_info(tz_key: str = DEFAULT_TIMEZONE_KEY) -> dict:
    return TIMEZONE_CONFIG.get(tz_key, TIMEZONE_CONFIG[DEFAULT_TIMEZONE_KEY])

def get_timezone_display_name(tz_key: str, lang: str = "zh_CN") -> str:
    info = get_timezone_info(tz_key)
    if lang == "en_US":
        return info.get("display_name_en", info.get("display_name_zh"))
    return info.get("display_name_zh")

def timestamp_to_target_datetime(ms_timestamp: int, tz_key: str = DEFAULT_TIMEZONE_KEY) -> datetime:
    sec_timestamp = ms_timestamp / 1000.0
    dt_utc = datetime.fromtimestamp(sec_timestamp, tz=UTC_TZ)
    target_tz = get_timezone_info(tz_key)["tz"]
    return dt_utc.astimezone(target_tz)

def format_to_iso(dt: datetime) -> str:
    return dt.isoformat()

def get_current_timezone() -> str:
    try:
        from utils.time_utils import DEFAULT_TIMEZONE_KEY
        return DEFAULT_TIMEZONE_KEY
    except ImportError:
        return "Asia/Shanghai"