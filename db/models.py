from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.String(36), primary_key=True)  # Task ID
    filename = db.Column(db.String(255), nullable=False)  # 原始文件名
    mnemonic_name = db.Column(db.String(200), nullable=True)   # 助记名 上传日志后 可以在列表页增加这个名字用来辅助记住这个日志是什么方便后续查看而不是记文件名
    analysis_timezone = db.Column(db.String(100), nullable=True)  # 解析时使用的时区
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

class S_Settings(db.Model):
    __tablename__ = 's_settings'
    id = db.Column(db.Integer, primary_key=True)
    setting_name = db.Column(db.String(100), nullable=False)
    setting_key = db.Column(db.String(400), nullable=False)
    setting_value = db.Column(db.Text, nullable=True)