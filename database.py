from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base

# Замени ТВОЙ_ПАРОЛЬ на пароль от PostgreSQL!
DATABASE_URL = "postgresql+psycopg2://postgres:Ristik_pro1@localhost:5432/my_todo_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class TaskModel(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    done = Column(Boolean, default=False)
    priority = Column(Integer, default=1)

Base.metadata.create_all(bind=engine)