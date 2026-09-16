from flask import Flask, request, g, make_response, redirect, url_for
from utils.time_utils import TIMEZONE_CONFIG, get_timezone_display_name
from config.sys_config import (
    SQLALCHEMY_DATABASE_URI, 
    SQLALCHEMY_TRACK_MODIFICATIONS, 
    MAX_CONTENT_LENGTH,
    DEFAULT_LANGUAGE,
    SUPPORTED_LANGUAGES
)
from db.task_manager import init_db
from web.blueprints import upload_bp, tasks_bp, report_bp
from core.i18n_utils import init_i18n, t

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
    app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH

    init_db(app)

    @app.before_request
    def set_global_language():
        req_lang = request.args.get('lang') or request.cookies.get('lang') or DEFAULT_LANGUAGE
        
        if req_lang not in SUPPORTED_LANGUAGES:
            req_lang = DEFAULT_LANGUAGE

        g.lang = req_lang
        init_i18n(g.lang)

    @app.context_processor
    def inject_i18n():
        return dict(t=t, current_lang=getattr(g, 'lang', DEFAULT_LANGUAGE))

    @app.context_processor
    def inject_timezones():
        current_tz = request.cookies.get('user_timezone', 'Asia/Shanghai')
        return dict(timezones=TIMEZONE_CONFIG, get_tz_display=get_timezone_display_name, current_tz=current_tz)

    @app.route('/set_language/<lang_code>')
    def set_language(lang_code):
        if lang_code not in SUPPORTED_LANGUAGES:
            lang_code = DEFAULT_LANGUAGE
            
        redirect_url = request.referrer or '/'
        response = make_response(redirect(redirect_url))
        
        response.set_cookie('lang', lang_code, max_age=30*24*60*60, path='/')
        return response

    @app.route('/set_timezone/<path:tz_key>')
    def set_timezone(tz_key):
        redirect_url = request.referrer or url_for('tasks.task_list_page')
        response = make_response(redirect(redirect_url))
        response.set_cookie('user_timezone', tz_key, max_age=30*24*3600, path='/')
        return response

    app.register_blueprint(upload_bp)
    app.register_blueprint(tasks_bp)
    app.register_blueprint(report_bp)

    return app