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

DEFAULT_LANGUAGE = "en_US"
SUPPORTED_LANGUAGES = ["zh_CN", "en_US"]

MAX_TASK_COUNT = 50
