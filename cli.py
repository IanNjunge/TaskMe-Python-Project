#main menu for user interactions
from database import SessionLocal
from models import Task, Category
from datetime import datetime

session = SessionLocal()

def menu():
    print("TaskMe")
    print("1. New Task")
    print("2. My Tasks")
    print("3. Update Task Status")
    print("4. Delete Task")
    print("5. Exit TaskMe")
    
def add_task():
    title = input("Task title: ")    
    description = input("Describe task: ")
    due = input("Due date (YYYY-MM-DD): ")
    
    category_name = input("Category: ")
    category = session.query(Category).filter_by(name=category_name).first()