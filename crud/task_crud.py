from models.task import Task

task_list: list[Task] = []

def create_task(task:Task):
    task_list.append(task)
    return {"message":"Task Created Successfully","task":task}

def get_tasks():
    return task_list

def get_task_by_id(task_id:int):
    for task in task_list:
        if task.id == task_id:
            return task
        else:
            return {"error":"Task Not Found"}

def update_task(task_id: int, updated_task: Task):
    for index,task in enumerate(task_list):
        if task.id == task_id:
            task_list[index] = updated_task
            return {"message":"Task Updated Successfully","task":updated_task}
    return {"error":"Task Not Found"}

def delete_task(task_id: int):
    for task in task_list:
        if task.id == task_id:
            task_list.remove(task)
            return {"message": f"Task {task_id} deleted"}
    return {"error": "Task not found"}