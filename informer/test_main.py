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
