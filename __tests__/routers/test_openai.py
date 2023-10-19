from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_chat_completion():
    res = client.post("/api/openai/chat_completion", params={"message": "你好"})
    assert res.status_code == 200
    assert isinstance(res.json(), dict)
