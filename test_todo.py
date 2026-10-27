from fastapi.testclient import TestClient
from todo import app

client = TestClient(app)


def test_read_root():
    """Проверяем, что сервер отвечает на корневой запрос."""
    response = client.get("/")
    # Пока у нас нет эндпоинта на "/", но мы можем проверить, что сервер жив
    # Если у тебя есть эндпоинт "/", проверь его
    assert response.status_code in [200, 404]


def test_create_task():
    """Проверяем, что задача создается."""
    response = client.post("/tasks", json={"title": "Тестовая задача", "priority": 3})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Тестовая задача"
    assert data["priority"] == 3
    assert data["id"] is not None


def test_get_tasks():
    """Проверяем, что список задач возвращается."""
    response = client.get("/tasks")
    assert response.status_code == 200
    assert isinstance(response.json(), list)