import uuid

def generate_task_id() -> str:
    return str(uuid.uuid4())