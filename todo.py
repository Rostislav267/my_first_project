from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import SessionLocal, TaskModel, engine, Base
from sqlalchemy import func

app = FastAPI()

# Создаем таблицы (на всякий случай, если их нет)
Base.metadata.create_all(bind=engine)

# Схема данных для создания задачи (то, что присылает клиент)
class TaskCreate(BaseModel):
    title: str
    priority: int=1
    done: bool=False

# Функция для получения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/tasks")
def get_all_tasks(db: Session = Depends(get_db), sort_by_priority: bool=False, skip: int=0, limit: int=10):
    query = db.query(TaskModel)
    if sort_by_priority == True:
        query = query.order_by(TaskModel.priority.desc())
    tasks = query.offset(skip).limit(limit).all()
    return tasks

@app.get("/tasks/{task_id}")
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    return task

@app.post("/tasks")
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    # Создаем объект модели
    new_task = TaskModel(title=task.title, priority=task.priority)
    # Добавляем в базу и сохраняем
    db.add(new_task)
    db.commit()
    db.refresh(new_task)  # Обновляем объект, чтобы получить его ID из базы
    return new_task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    db.delete(task)
    db.commit()
    return {"message": "Задача удалена"}

@app.put("/tasks/{task_id}")
def put_task(task_id: int, task_data: TaskCreate, db: Session = Depends(get_db)):
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    task.title = task_data.title
    task.priority = task_data.priority
    task.done = task_data.done
    db.commit()
    return task

@app.get("/tasks/search")
def search_tasks(query: str, db: Session = Depends(get_db)):
    tasks = db.query(TaskModel).filter(
        func.lower(TaskModel.title).contains(query.lower())
    ).all()
    return tasks

@app.get("/tasks/filter")
def done_tasks(done: bool, db: Session = Depends(get_db)):
    tasks = db.query(TaskModel).filter(TaskModel.done == done).all()
    return tasks

