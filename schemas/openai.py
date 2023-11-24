from typing import Any

from pydantic import BaseModel


class ResOpenAIChatCompletion(BaseModel):
    id: str
    choices: list[dict[str, Any]]
    created: int
    model: str
    object: str
    usage: dict[str, int]
