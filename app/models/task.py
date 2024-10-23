from fastapi import APIRouter
from backend.db import Base
from sqlalchemy.orm import Session
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship
from typing import Annotated
from models import *
from schemas import CreateTask, UpdateTask
from sqlalchemy import insert, select, update, delete
from slugify import slugify
from backend.db_depends import get_db


class Task(Base):
    __tablename__ = "tasks"
    __table_agrs__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("tasks.id"), nullable=True, index=True)
    slug = Column(String, unique=True, index=True)
    user = relationship("User", back_populates="tasks")


# from sqlalchemy.schema import CreateTable
# print(CreateTable(Task.__table__))
