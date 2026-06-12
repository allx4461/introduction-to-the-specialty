from fastapi.testclient import TestClient
import sys
import os

# Add informer directory to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from main import app  # noqa: E402

client = TestClient(app)


def test_get_excuse():
    response = client.get("/excuse")
    assert response.status_code == 200
    assert "excuse" in response.json()


def test_post_and_get_messages():
    # 1. Отправляем сообщение
    post_response = client.post(
        "/messages",
        json={"username": "Тестер", "text": "Привет из автотеста!"}
    )
    assert post_response.status_code == 200
    assert post_response.json() == {"status": "ok"}

    # 2. Получаем сообщения и проверяем наличие
    get_response = client.get("/messages")
    assert get_response.status_code == 200

    messages = get_response.json()
    assert len(messages) >= 1

    # Ищем наше сообщение в списке
    found = False
    for msg in messages:
        if (msg["username"] == "Тестер" and
                msg["text"] == "Привет из автотеста!"):
            found = True
            break

    assert found is True
