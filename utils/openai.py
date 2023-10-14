import openai
from typing import Union
from utils.env import *

openai.api_type = OPENAI_API_TYPE
openai.api_base = OPENAI_API_ENDPOINT
openai.api_key = OPENAI_API_KEY
openai.api_version = OPENAI_API_VERSION


def chat_completion(messages: list, model: str = GPT35_TURBO_COMPLETIONS_MODEL, temperature: Union[int, float] = 0):
    res = openai.ChatCompletion.create(
        engine=model, messages=messages, temperature=temperature)
    return {"res": res, "content": res['choices'][0]["message"]["content"]}
