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
    
def add_tasks():
    name = input("Task name: ")    
    description = input("Describe task: ")
    due = input("Due date (YYYY-MM-DD): ")
    
    category_name = input("Category: ")
    category = session.query(Category).filter_by(name=category_name).first()
    if not category:
        category = Category(name=category_name)
        session.add(category)
        session.commit()
        
        
    task = Task(
        title = name,
        description = description,
        due = datetime.strptime(due, "%Y-%m-%d"),
        category = category
        )
    
    session.add(task)
    session.commit()
    print("Task added!")
    
def view_tasks():
    tasks = session.query(Task).all()
    if not tasks:
        print("No tasks found.")
        return
    for t in tasks:
         print(f"[{t.id}] - {t.title} - {t.status} - {t.category.name} - (Due{t.due})")
         
def update_tasks():
    task_id = int(input("Task ID to update: "))
    task = session.query(Task).get(task_id)    
    if task:
        task.status = input("(Pending/Done): ")
        session.commit()     
        print("Task updated!")
    else:
        print("Task not found.")      
        
def delete_tasks():
    task_id = int(input("Task ID to delete: "))
    task = session.query(Task).get(task_id)
    if task:
        session.delete(task)
        session.commit()
        print("Tasks deleted!")
    else:
        print("Task not found.") 
        
        

#The main loop
def main():
    while True:
        menu()
        choice = input("Choose: ")
        if choice == "1":
            add_tasks()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_tasks()
        elif choice == "4":
            delete_tasks()
        elif choice == "5":
            print("Exiting.")
            break
        else:
            print("Invalid choice")     
                     
if __name__ == "__main__":
    main()                     
    
     