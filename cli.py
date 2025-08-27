#main menu for user interactions
from database import SessionLocal
from models import Task, Category
from datetime import datetime

session = SessionLocal()

def menu():
    print("TaskMe")