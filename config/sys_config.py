import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DB_DIR = os.path.join(BASE_DIR, 'db', 'data')
os.makedirs(DB_DIR, exist_ok=True)
SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(DB_DIR, 'app.db')}"
SQLALCHEMY_TRACK_MODIFICATIONS = False

STORAGE_DIR = os.path.join(BASE_DIR, 'storage')
STORAGE_UPLOADS_DIR = os.path.join(STORAGE_DIR, 'uploads')
STORAGE_RESULTS_DIR = os.path.join(STORAGE_DIR, 'results')

os.makedirs(STORAGE_UPLOADS_DIR, exist_ok=True)
os.makedirs(STORAGE_RESULTS_DIR, exist_ok=True)

MAX_CONTENT_LENGTH = 100 * 1024 * 1024 
ALLOWED_EXTENSIONS = {'json'} 

# DEFAULT_LANGUAGE = "en_US"
SUPPORTED_LANGUAGES = ["zh_CN", "en_US"]

# 允许的最多条上传、解析完、等待解析的日志数量
MAX_TASK_COUNT = 50
# 允许同时解析最大的线程数 默认为3 测试20没有出现异常，CPU是7735U
MAX_ANALYSIS_THREAD = 3
# 解析的线程队列 完了就移除
LIST_ANALYSIS_QUEUE= []

DEFAULT_LANGUAGE_KEY = "default_language"
DEFAULT_LANGUAGE_NAME = "default language"
DEFAULT_LANGUAGE_VALUE = ""
DEFAULT_LANGUAGE = "zh_CN"

DEFAULT_TIMEZONE_KEY = "default_timezone"
DEFAULT_TIMEZONE_NAME = "default timezone"
DEFAULT_TIMEZONE_VALUE= ""
DEFAULT_TIMEZONE = ""
