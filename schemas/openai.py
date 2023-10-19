from pydantic import BaseModel


class ResOpenAIChatCompletion(BaseModel):
    id: str
    choices: list
    created: int
    model: str
    object: str
    usage: dict


class ChatCompletion(BaseModel):
    res: ResOpenAIChatCompletion
    content: str
