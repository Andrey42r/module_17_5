from backend.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"
    __table_agrs__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(String)
    slug = Column(String, unique=True, index=True)
    task = relationship("Task", back_populates='user')

#
# # from sqlalchemy.schema import CreateTable
# # print(CreateTable(User.__table__))
