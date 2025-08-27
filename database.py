from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


engine = create_engine("sqlite:///taskme.db", echo=True)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)