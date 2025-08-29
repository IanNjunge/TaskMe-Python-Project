#main menu for user interactions
from database import SessionLocal, engine
from models import Task, Category, Base, User
from datetime import datetime

#cli menu
def menu():
    print("TaskMe")
    print("1. New Task")
    print("2. My Tasks")
    print("3. Update Task Status")
    print("4. Delete Task")
    print("5. Exit TaskMe")

#task functions  
def add_tasks(session, user):
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
        category = category,
        user_id = user.id
        )
    
    session.add(task)
    session.commit()
    print("Task added!")
    
def view_tasks(session, user):
    tasks = session.query(Task).filter_by(user_id=user.id).all()
    if not tasks:
        print("No tasks found.")
        return
    for t in tasks:
         print(f"[{t.id}] - {t.title} - {t.status} - {t.category.name} - (Due{t.due})")
         
def update_tasks(session, user):
    view_tasks(session, user)
    task_id = int(input("Task ID to update: "))
    task = session.query(Task).get(task_id)    
    if task:
        task.status = input("(Pending/Done): ")
        session.commit()     
        print("Task updated!")
    else:
        print("Task not found or belongs to another user.")      
        
def delete_tasks(session, user):
    view_tasks(session, user)
    task_id = int(input("Task ID to delete: "))
    task = session.query(Task).filter_by(id=task_id, user=user.id).first()
    if task:
        session.delete(task)
        session.commit()
        print("Tasks deleted!")
    else:
        print("Task not found or belongs to another user.") 
        
        
#login/register
def login(session):
    print("Welcome to TaskMe!")
    username = input("Enter your username: ").strip()

    #Is user new?
    user = session.query(User).filter_by(username=username).first()
    if not user:
        print("Welcome new user! Creating account....")
        user = User(username=username)
        session.add(user)
        session.commit() 
        print(f"Welcome: {user.username}")
    else:    
        print(f"Welcome back, {user.usermame}!")
    
    return user    


def main():
    Base.metadata.create_all(bind=engine)
    session = SessionLocal() 
    user = login(session)
    
    #The main menu loop
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
    
    session.close()         
                     
if __name__ == "__main__":
    main()                     
    
     