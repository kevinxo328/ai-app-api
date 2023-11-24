from typing import Any, Union

from pydantic import BaseModel

import utils.env as env


class ResOpenAIChatCompletion(BaseModel):
    id: str
    choices: list[dict[str, Any]]
    created: int
    model: str
    object: str
    usage: dict[str, int]


class ReqChatCompletion(BaseModel):
    user_prompt: str
    temperature: Union[int, float] = 0
    model: str = env.GPT35_MODEL
    sys_prompt: str = ""
