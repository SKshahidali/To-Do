from fastapi import FastAPI
from routes import task_routes
from db.database import Base, engine
from models.task_model import TaskModel

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(task_routes.router)
