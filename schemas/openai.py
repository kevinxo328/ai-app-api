from pydantic import BaseModel


class ResOpenAIChatCompletion(BaseModel):
    id: str
    choices: list
    created: int
    model: str
    object: str
    usage: dict
