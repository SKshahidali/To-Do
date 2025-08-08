from pydantic import BaseModel

class Task(BaseModel):
    id: int
    title: str
    body: str
    completed: bool = False