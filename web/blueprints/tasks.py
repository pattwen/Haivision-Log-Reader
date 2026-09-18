import shutil
import os
import math
import threading
from flask import Blueprint, render_template, jsonify, current_app, request
from db.task_manager import get_all_tasks, get_task_by_id, update_task_status, delete_task, update_task_mnemonic
from utils.time_utils import get_current_timezone
from core.log_processor import process_log_task
from config.sys_config import STORAGE_UPLOADS_DIR, STORAGE_RESULTS_DIR
from core.i18n_utils import t as lag

tasks_bp = Blueprint('tasks', __name__)

def async_analyze_log(app, task_id: str, target_tz_key: str = 'Asia/Shanghai'):
    with app.app_context():
        try:
            update_task_status(task_id, status='Processing')
            process_log_task(task_id, target_tz_key=target_tz_key)
            update_task_status(task_id, status='Completed', analysis_timezone=target_tz_key)
        except Exception as e:
            error_msg = str(e)
            print(f"[{task_id}] {lag('htmlreturn.analysis_task_error')} {error_msg}")
            update_task_status(task_id, status='Failed', error_msg=error_msg)

@tasks_bp.route('/tasks', methods=['GET'])
def task_list_page():
    page = request.args.get('page', 1, type=int)
    per_page = 10
    all_tasks = get_all_tasks()
    total_tasks = len(all_tasks)
    total_pages = math.ceil(total_tasks / per_page) if total_tasks > 0 else 1
    if page < 1:
        page = 1
    elif page > total_pages:
        page = total_pages
    start = (page - 1) * per_page
    end = start + per_page
    tasks = all_tasks[start:end]
    return render_template('task_list.html', tasks=tasks, current_page=page, total_pages=total_pages, total_tasks=total_tasks)

@tasks_bp.route('/api/tasks', methods=['GET'])
def get_tasks_api():
    tasks = get_all_tasks()
    return jsonify({'success': True, 'tasks': [t.to_dict() for t in tasks]})

@tasks_bp.route('/api/tasks/<task_id>/analyze', methods=['POST'])
def trigger_analysis(task_id):
    task = get_task_by_id(task_id)
    if not task:
        return jsonify({'success': False, 'message': lag('htmlreturn.mission_notexist')}), 404

    if task.status == 'Processing':
        return jsonify({'success': False, 'message': lag('htmlreturn.mission_analysing')}), 400
    
    if task.status == 'Completed':
        return jsonify({'success': False, 'message': lag('htmlreturn.mission_analyzed')}), 400
    
    user_tz = request.cookies.get('user_timezone', get_current_timezone() or 'Asia/Shanghai')
    app = current_app._get_current_object()
    thread = threading.Thread(target=async_analyze_log, args=(app, task_id, user_tz))
    thread.start()

    return jsonify({'success': True, 'message': lag('htmlreturn.mission_started'), 'task_id': task_id})

@tasks_bp.route('/api/tasks/<task_id>', methods=['DELETE'])
def remove_task(task_id):
    task = get_task_by_id(task_id)
    if not task:
        return jsonify({'success': False, 'message': lag('htmlreturn.mission_notexist')}), 404

    delete_task(task_id)

    upload_path = os.path.join(STORAGE_UPLOADS_DIR, task_id)
    result_path = os.path.join(STORAGE_RESULTS_DIR, task_id)

    if os.path.exists(upload_path):
        shutil.rmtree(upload_path, ignore_errors=True)
    if os.path.exists(result_path):
        shutil.rmtree(result_path, ignore_errors=True)

    return jsonify({'success': True, 'message': lag('htmlreturn.mission_file_deleted')})

@tasks_bp.route('/api/tasks/<task_id>/mnemonic', methods=['POST'])
def update_mnemonic(task_id):
    data = request.get_json() or {}
    mnemonic_name = data.get('mnemonic_name', '')
    
    success = update_task_mnemonic(task_id, mnemonic_name)
    if success:
        return jsonify({'status': 'success', 'message': 'Mnemonic updated successfully'})
    return jsonify({'status': 'error', 'message': 'Task not found'}), 404