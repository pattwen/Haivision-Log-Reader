import os
from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from werkzeug.utils import secure_filename
from config.sys_config import STORAGE_UPLOADS_DIR, ALLOWED_EXTENSIONS, MAX_TASK_COUNT
from utils.id_generator import generate_task_id
from db.task_manager import create_task, get_all_tasks_count
from core.i18n_utils import t as lag

upload_bp = Blueprint('upload', __name__)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@upload_bp.route('/', methods=['GET'])
@upload_bp.route('/upload', methods=['GET'])
def upload_page():
    return render_template('upload.html')

@upload_bp.route('/api/upload', methods=['POST'])
def handle_upload():
    if 'file' not in request.files:
        return jsonify({'success': False, 'message': lag('htmlreturn.upload_file_notexist')}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'success': False, 'message': lag('htmlreturn.upload_file_notselect')}), 400
    
    if get_all_tasks_count() >= MAX_TASK_COUNT:
        return jsonify({'success': False, 'message': lag('htmlreturn.max_task_count')}), 400
    
    if file and allowed_file(file.filename):
        task_id = generate_task_id()
        original_filename = secure_filename(file.filename) or file.filename

        task_upload_dir = os.path.join(STORAGE_UPLOADS_DIR, task_id)
        os.makedirs(task_upload_dir, exist_ok=True)

        save_path = os.path.join(task_upload_dir, 'log.json')
        file.save(save_path)

        task = create_task(task_id=task_id, filename=original_filename)

        return jsonify({
            'success': True,
            'message': lag('htmlreturn.upload_file_success'),
            'task': task.to_dict()
        })

    return jsonify({'success': False, 'message': lag('htmlreturn.upload_file_supportonly')}), 400