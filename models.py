from sqlalchemy import Integer, String, Date, Column, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Category(Base):
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    
    tasks = relationship("Task", "category")
    
class Task(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    due = Column(Date)
    status = Column(String, default = "Pending")
    
    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship("Category", back_populates="tasks")
    
    if __name__ == "__main__":
        from database import engine
        Base.metadata.create_all(engine)