from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_chat_completion():
    response = client.post("/api/openai/chat_completion")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
