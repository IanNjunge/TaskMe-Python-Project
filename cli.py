#main menu for user interactions
from database import SessionLocal
from models import Task, Category
from datetime import datetime

session = SessionLocal()

#menu
def menu():
    print("TaskMe")
    print("1. New Task")
    print("2. My Tasks")
    print("3. Update Task Status")
    print("4. Delete Task")
    print("5. Exit TaskMe")
    
def add_task():
    name = input("Task name: ")    
    description = input("Describe task: ")
    due = input("Due date (YYYY-MM-DD): ")
    
    category_name = input("Category: ")
    category = session.query(Category).filter_by(name=category_name).first()
    if not category:
        category = Category(name=category_name)
        session.add(category)
        
        
    task = Task(
        name = name,
        description = description,
        due = datetime.striptime(due, "%Y-%m-%d"),
        category = category)
    
    session.add(task)
    session.commit()
    print("Task added!")
    
def view_tasks():
    tasks = session.query(Task).all()
    if not tasks:
        print("No tasks found.")
        return
    for t in tasks:
         print(f"[{t.id}] - {t.name} - {t.status} - {t.category.name} - (Due{t.due})")
         
def update_task():
    task_id = int(input("Task ID to update: "))
    task = session.query(Task).get(task_id)    
    if task:
        task.status = input("(Pending/Done): ")
        session.commit()     
        print("Task updated!")
    else:
        print("Task not found.")      
        
    
    
     