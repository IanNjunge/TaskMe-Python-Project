#sqlalchemy imports, orm models

from sqlalchemy import Integer, String, Date, Column, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

#models
class Category(Base):
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    
    tasks = relationship("Task", back_populates="category")
    
class Task(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    due = Column(Date)
    status = Column(String, default = "Pending")
    
    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship("Category", back_populates="tasks")
    
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="tasks") 
    
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    
    tasks = relationship("Task", back_populates="user")    