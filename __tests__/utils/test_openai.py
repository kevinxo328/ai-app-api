import schemas.openai as OpenAISchema
import utils.openai as openai


def test_chat_completion(mocker):
    prompts = [{"role": "user", "content": "你好"}]
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
        "openai.ChatCompletion.create", return_value=return_value
    )
    res = openai.chat_completion(prompts)

    assert mock_chat_completion.call_count == 1
    assert (
        res.model_dump()["content"] == return_value["choices"][0]["message"]["content"]
    )
