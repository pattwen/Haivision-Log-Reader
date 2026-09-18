import os
import json
import config.sys_config as config

_raw_lang = getattr(config, 'DEFAULT_LANGUAGE', 'zh_CN')
if isinstance(_raw_lang, list):
    CURRENT_LANG = _raw_lang[0] if len(_raw_lang) > 0 else "zh_CN"
else:
    CURRENT_LANG = str(_raw_lang) if _raw_lang else "zh_CN"

LANG_DATA = {}

def get_current_lang() -> str:
    global CURRENT_LANG
    if isinstance(CURRENT_LANG, list):
        return CURRENT_LANG[0] if len(CURRENT_LANG) > 0 else "zh_CN"
    return str(CURRENT_LANG) if CURRENT_LANG else "zh_CN"

def init_i18n(lang_code: str = "zh_CN") -> None:
    global CURRENT_LANG, LANG_DATA
    
    if isinstance(lang_code, list):
        lang_code = lang_code[0] if len(lang_code) > 0 else "zh_CN"
        
    CURRENT_LANG = str(lang_code) if lang_code else "zh_CN"
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    lang_file_path = os.path.join(base_dir, "language", f"{CURRENT_LANG}.json")
    
    if os.path.exists(lang_file_path):
        with open(lang_file_path, "r", encoding="utf-8") as f:
            LANG_DATA = json.load(f)
    else:
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