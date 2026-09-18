import re
from config import sys_config
from db.models import S_Settings,  db

# 设置功能暂时不加

CONFIG_MAP = {
    "default_language": "DEFAULT_LANGUAGE_VALUE",
    "default_timezone": "DEFAULT_TIMEZONE_VALUE"
}


def parse_to_list(value):
    if not value:
        return []
    return [x.strip() for x in value.split(",") if x.strip()]


def normalize_input(value):
    if not value:
        return ""

    items = re.split(r'[\n,，]+', value)

    result = []
    seen = set()

    for item in items:
        item = item.strip()
        if item and item not in seen:
            result.append(item)
            seen.add(item)

    return ",".join(result)


def load_sys_config_from_db():
    print("Loading system configuration from database...")
    rows = S_Settings.query.all()

    for row in rows:
        if row.setting_key in CONFIG_MAP:
            print(f"Loading setting: {row.setting_key} = {row.setting_value}")
            setattr(
                sys_config,
                CONFIG_MAP[row.setting_key],
                row.setting_value or ""
            )


def put_sys_config_to_context():
    print("Putting system configuration to context...")
    for key, attr in CONFIG_MAP.items():
        value = getattr(sys_config, attr)

        setattr(
            sys_config,
            attr.replace("_VALUE", ""),
            parse_to_list(value)
        )