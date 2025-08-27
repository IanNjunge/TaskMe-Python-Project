#db connection setup
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

DB_FILE = "taskme.db"
DB_URL = f"sqlite:///{DB_FILE}"

engine = create_engine("sqlite:///taskme.db", echo=True) #create engine
SessionLocal = sessionmaker(bind=engine) #create session
Base = declarative_base()

if not os.path.exists(DB_FILE):
    Base.metadata.create_all(bind=engine)
    print(f"Database '{DB_FILE}' created.")