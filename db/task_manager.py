# db/task_manager.py
import os
from typing import List, Optional
from flask import Flask
from db.models import db, Task
from config.sys_config import SQLALCHEMY_DATABASE_URI
from core.i18n_utils import t as lag

def init_db(app: Flask) -> None:
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    
    with app.app_context():
        db.create_all()
        print(f"[Database] {lag('consolelog.DB_connect_done')}")

def create_task(task_id: str, filename: str) -> Task:
    task = Task(
        id=task_id,
        filename=filename,
        status='Pending'
    )
    db.session.add(task)
    db.session.commit()
    return task

def get_task_by_id(task_id: str) -> Optional[Task]:
    return db.session.get(Task, task_id)

def get_all_tasks() -> List[Task]:
    return Task.query.order_by(Task.created_at.desc()).all()

def get_all_tasks_count() -> int:
    return Task.query.count()

def update_task_status(task_id: str, status: str, error_msg: Optional[str] = None) -> Optional[Task]:
    task = get_task_by_id(task_id)
    if task:
        task.status = status
        if error_msg is not None:
            task.error_msg = error_msg
        db.session.commit()
    return task

def delete_task(task_id: str) -> bool:
    task = get_task_by_id(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
        return True
    return False