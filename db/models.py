from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.String(36), primary_key=True)  # Task ID (UUID)
    filename = db.Column(db.String(255), nullable=False)  # 用户原始文件名
    status = db.Column(db.String(20), nullable=False, default='Pending')  # Pending / Processing / Completed / Failed
    error_msg = db.Column(db.Text, nullable=True)  # 失败时的错误日志
    created_at = db.Column(db.DateTime, default=datetime.now)  # 上传时间
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)  # 完成/状态更新时间

    def to_dict(self):
        return {
            'id': self.id,
            'filename': self.filename,
            'status': self.status,
            'error_msg': self.error_msg,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S') if self.created_at else None,
            'updated_at': self.updated_at.strftime('%Y-%m-%d %H:%M:%S') if self.updated_at else None,
        }