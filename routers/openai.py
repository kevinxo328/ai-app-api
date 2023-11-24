from typing import Union

from fastapi import APIRouter, HTTPException

import schemas.openai as OpenAISchema
import utils.env as env
import utils.openai as openai

router = APIRouter(prefix="/api/openai", tags=["openai"])


# TODO: Global Exception https://stackoverflow.com/questions/61596911/catch-exception-globally-in-fastapi
@router.post("/chat_completion", response_model=OpenAISchema.ChatCompletion)
async def chat_completion(
    message: str, temperature: Union[int, float] = 0, model: str = env.GPT35_MODEL
):
    try:
        res: OpenAISchema.ChatCompletion = openai.chat_completion(
            messages=[
                {"role": "user", "content": message},
            ],
            temperature=temperature,
        )

        return OpenAISchema.ChatCompletion(**res)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/models", include_in_schema=False)
async def get_models():
    try:
        return openai.get_models_id()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
