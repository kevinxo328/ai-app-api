from fastapi.testclient import TestClient

import schemas.openai as OpenAISchema
from main import app

client = TestClient(app)


def test_chat_completion():
    res = client.post("/api/openai/chat_completion", params={"message": "你好"})
    assert res.status_code == 200
    assert isinstance(
        OpenAISchema.ChatCompletion(**res.json()), OpenAISchema.ChatCompletion
    )
