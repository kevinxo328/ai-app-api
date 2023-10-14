from typing import Union

import openai
import utils.env as env

openai.api_type = env.OPENAI_API_TYPE
openai.api_base = env.OPENAI_API_ENDPOINT
openai.api_key = env.OPENAI_API_KEY
openai.api_version = env.OPENAI_API_VERSION


def chat_completion(
    messages: list,
    model: str = env.GPT35_TURBO_COMPLETIONS_MODEL,
    temperature: Union[int, float] = 0,
):
    res = openai.ChatCompletion.create(
        engine=model, messages=messages, temperature=temperature
    )
    return {"res": res, "content": res["choices"][0]["message"]["content"]}
