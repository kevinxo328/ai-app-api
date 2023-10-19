from typing import Union

from fastapi import APIRouter, HTTPException

import schemas.openai as OpenAISchema
import utils.openai as openai

router = APIRouter(prefix="/api/openai", tags=["openai"])


@router.post("/chat_completion", response_model=OpenAISchema.ChatCompletion)
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
