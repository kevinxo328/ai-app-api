from typing import Union

import utils.openai as openai
from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/api/openai", tags=["openai"])


@router.post("/chat_completion")
async def chat_completion(message: str, temperature: Union[int, float] = 0):
    try:
        return openai.chat_completion(
            messages=[
                {"role": "user", "content": message},
            ],
            temperature=temperature,
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
