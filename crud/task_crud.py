from models.task import Task
from sqlalchemy.orm import Session
from models.task_model import TaskModel


def create_task(db:Session,task:Task):
    db_task = TaskModel(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_tasks(db:Session):
    return db.query(TaskModel).all()

def get_task_by_id(db:Session,task_id:int):
    return db.query(TaskModel).filter(TaskModel.id == task_id).first()

def update_task(db:Session,task_id: int, updated_task: Task):
    db_task = get_task_by_id(db, task_id)
    if db_task:
        for key, value in updated_task.dict().items():
            setattr(db_task, key, value)
        db.commit()
        db.refresh(db_task)
        return db_task
    return None

def delete_task(db:Session,task_id: int):
    db_task = get_task_by_id(db, task_id)
    if db_task:
        db.delete(db_task)
        db.commit()
        return True
    return False