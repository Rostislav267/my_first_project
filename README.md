# To-Do API

Простой REST API для управления списком задач, написанный на **FastAPI** с использованием **PostgreSQL** и **SQLAlchemy**.

## 🚀 Функционал

- Создание задач (с приоритетом)
- Просмотр всех задач
- Просмотр одной задачи по ID
- Обновление задачи (название, приоритет, статус выполнения)
- Удаление задачи
- Поиск задач по названию (без учета регистра)
- Фильтрация по статусу выполнения (`done`)
- Сортировка по приоритету
- Пагинация (skip, limit)

## 🛠️ Технологии

- Python 3.13
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pytest (тесты)

## 📦 Установка и запуск

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/Rostislav267/my_first_project.git
   cd my_first_project
   
python -m venv venv
# Windows:
.\venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

pip install -r requirements.txt

uvicorn todo:app --reload


