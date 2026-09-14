from datetime import datetime
import pytz

UTC_TZ = pytz.utc
BEIJING_TZ = pytz.timezone("Asia/Shanghai")

TZ_UTC_0   = pytz.utc                                 
TZ_LONDON  = pytz.timezone("Europe/London")           

TZ_WEST_11 = pytz.timezone("Pacific/Pago_Pago")
TZ_WEST_10 = pytz.timezone("Pacific/Honolulu")
TZ_WEST_9  = pytz.timezone("America/Anchorage")
TZ_WEST_8  = pytz.timezone("America/Los_Angeles")
TZ_WEST_7  = pytz.timezone("America/Denver")
TZ_WEST_6  = pytz.timezone("America/Chicago")
TZ_WEST_5  = pytz.timezone("America/New_York")
TZ_WEST_4  = pytz.timezone("America/Santiago")
TZ_WEST_3  = pytz.timezone("America/Argentina/Buenos_Aires")
TZ_WEST_2  = pytz.timezone("America/Noronha")
TZ_WEST_1  = pytz.timezone("Atlantic/Cape_Verde")

TZ_EAST_1  = pytz.timezone("Europe/Paris")
TZ_EAST_2  = pytz.timezone("Europe/Kyiv")
TZ_EAST_3  = pytz.timezone("Europe/Moscow")
TZ_EAST_4  = pytz.timezone("Asia/Dubai")
TZ_EAST_5  = pytz.timezone("Asia/Karachi")
TZ_EAST_6  = pytz.timezone("Asia/Dhaka")
TZ_EAST_7  = pytz.timezone("Asia/Bangkok")
TZ_EAST_8  = pytz.timezone("Asia/Shanghai")
TZ_EAST_9  = pytz.timezone("Asia/Tokyo")
TZ_EAST_10 = pytz.timezone("Australia/Sydney")
TZ_EAST_11 = pytz.timezone("Pacific/Noumea")
TZ_EAST_12 = pytz.timezone("Pacific/Auckland")

TZ_INDIA   = pytz.timezone("Asia/Kolkata")
TZ_IRAN    = pytz.timezone("Asia/Tehran")
TZ_HK      = pytz.timezone("Asia/Hong_Kong")
TZ_SG      = pytz.timezone("Asia/Singapore")

def timestamp_to_bj_datetime(ms_timestamp: int) -> datetime:
    sec_timestamp = ms_timestamp/1000.0
    dt_utc = datetime.fromtimestamp(sec_timestamp, tz=UTC_TZ)
    dt_beijing = dt_utc.astimezone(BEIJING_TZ)
    return dt_beijing

def timestamp_to_tzTime(ms_timestamp:int,timezone:pytz.timezone = TZ_EAST_8) -> datetime:
    sec_timestamp = timezone/1000.0
    dt_utc = datetime.fromtimestamp(sec_timestamp, tz=TZ_UTC_0)
    dt_beijing = dt_utc.astimezone(TZ_EAST_8)
    return dt_beijing


def format_to_iso(dt: datetime) -> str:
    return dt.isoformat()