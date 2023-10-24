from typing import Union

import openai

import schemas.openai as OpenAISchema
import utils.env as env

openai.api_type = env.OPENAI_API_TYPE
openai.api_base = env.OPENAI_API_ENDPOINT
openai.api_key = env.OPENAI_API_KEY
openai.api_version = env.OPENAI_API_VERSION


def chat_completion(
    messages: list,
    model: str = env.GPT35_TURBO_COMPLETIONS_MODEL,
    temperature: Union[int, float] = 0,
) -> OpenAISchema.ChatCompletion:
    openai_chat_completion = openai.ChatCompletion.create(
        engine=model, messages=messages, temperature=temperature
    )

    res = {
        "res": openai_chat_completion,
        "content": openai_chat_completion["choices"][0]["message"]["content"],
    }

    return OpenAISchema.ChatCompletion(**res).model_dump()
