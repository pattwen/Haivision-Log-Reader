import shutil
import os
import threading
from flask import Blueprint, render_template, jsonify, current_app

from db.task_manager import get_all_tasks, get_task_by_id, update_task_status, delete_task
from core.log_processor import process_log_task
from config.sys_config import STORAGE_UPLOADS_DIR, STORAGE_RESULTS_DIR
from core.i18n_utils import t as lag

tasks_bp = Blueprint('tasks', __name__)

def async_analyze_log(app, task_id: str):
    with app.app_context():
        try:
            update_task_status(task_id, status='Processing')
            process_log_task(task_id)
            update_task_status(task_id, status='Completed')
        except Exception as e:
            error_msg = str(e)
            print(f"[{task_id}] {lag('htmlreturn.analysis_task_error')} {error_msg}")
            update_task_status(task_id, status='Failed', error_msg=error_msg)

@tasks_bp.route('/tasks', methods=['GET'])
def task_list_page():
    tasks = get_all_tasks()
    return render_template('task_list.html', tasks=tasks)

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

    app = current_app._get_current_object()

    thread = threading.Thread(target=async_analyze_log, args=(app, task_id))
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