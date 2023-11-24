from fastapi.testclient import TestClient

import schemas.openai as OpenAISchema
from main import app

client = TestClient(app)


def test_chat_completion(mocker):
    mock_data = {
        "id": "chatcmpl-abc123",
        "object": "chat.completion",
        "created": 1677858242,
        "model": "gpt-3.5-turbo-0613",
        "usage": {"prompt_tokens": 13, "completion_tokens": 7, "total_tokens": 20},
        "choices": [
            {
                "message": {"role": "assistant", "content": "This is a test!"},
                "finish_reason": "stop",
                "index": 0,
            }
        ],
    }

    return_value = OpenAISchema.ResOpenAIChatCompletion(**mock_data).model_dump()

    mock_chat_completion = mocker.patch(
        "utils.openai.chat_completion", return_value=return_value
    )

    res = client.post("/api/openai/chat_completion", params={"message": "你好"})
    assert mock_chat_completion.call_count == 1
    assert res.status_code == 200
    assert (
        res.json()["choices"][0]["message"]["content"]
        == return_value["choices"][0]["message"]["content"]
    )
