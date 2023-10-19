# import schemas.openai as OpenAISchema
import utils.openai as openai


def test_chat_completion():
    prompts = [{"role": "user", "content": "你好"}]
    res = openai.chat_completion(prompts)
    assert isinstance(res, dict)
