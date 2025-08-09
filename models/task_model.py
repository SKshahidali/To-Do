from sqlalchemy import Column,Integer,String,Boolean
from db.database import Base


class TaskModel(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    body = Column(String, nullable=False)
    completed = Column(Boolean, default=False)