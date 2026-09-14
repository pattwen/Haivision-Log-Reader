import sys
import os
from waitress import serve
from web import create_app
from core.i18n_utils import t as lag

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

app = create_app()

if __name__ == '__main__':
    host = '0.0.0.0'
    port = 5678
    
    print("=" * 60)
    print(f"Haivision Log Reader Online")
    print("=" * 60)
    serve(app, host=host, port=port, threads=8)