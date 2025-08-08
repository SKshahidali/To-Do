from fastapi import FastAPI
from routes import task_routes

app = FastAPI()

# Include the task routes
app.include_router(task_routes.router)
