from fastapi import APIRouter
from models.task import Task
from crud.task_crud import create_task, delete_task, get_task_by_id, update_task
from crud.task_crud import get_tasks

router = APIRouter()

# Welcome Screen
@router.get("/")
def hello_world():
    return {"message": "Hello World"}

# Get all tasks
@router.get("/all")
def get_all_tasks():
    return get_tasks()

# Get Task by ID
@router.get("/tasks/{id}")
def get_taskbyid(id: int):
    return get_task_by_id(task_id=id)

# Create a new Task
@router.post("/new")
def create_new_task(task: Task):
    return create_task(task)

@router.put("/task/{id}")
def updatetask(id: int, updated_task: Task):
    return update_task(task_id=id, updated_task=updated_task)

# Delete a Task
@router.delete("/task/{id}")
def deletetask(id: int):
    return delete_task(task_id=id)
