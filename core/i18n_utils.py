import os
import json
import config.sys_config as config

CURRENT_LANG = config.DEFAULT_LANGUAGE
LANG_DATA = {}

def init_i18n(lang_code: str = "zh_CN") -> None:
    global CURRENT_LANG, LANG_DATA
    CURRENT_LANG = lang_code
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    lang_file_path = os.path.join(base_dir, "language", f"{lang_code}.json")
    
    if os.path.exists(lang_file_path):
        with open(lang_file_path, "r", encoding="utf-8") as f:
            LANG_DATA = json.load(f)
    else:
        print(f"[Warning] Language configuration file not found: {lang_file_path}，the key value will be used for display by default.")
        LANG_DATA = {}

def t(key_path: str, **kwargs) -> str:
    keys = key_path.split(".")
    val = LANG_DATA
    
    for k in keys:
        if isinstance(val, dict):
            val = val.get(k, key_path)
        else:
            return key_path
            
    if isinstance(val, str) and kwargs:
        try:
            return val.format(**kwargs)
        except KeyError:
            return val
            
    return str(val) if val is not None else key_path