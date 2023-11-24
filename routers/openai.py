from fastapi import APIRouter, HTTPException

import schemas.openai as OpenAISchema
import utils.openai as openai

router = APIRouter(prefix="/api/openai", tags=["openai"])


# TODO: Global Exception https://stackoverflow.com/questions/61596911/catch-exception-globally-in-fastapi
@router.post("/chat_completion", response_model=OpenAISchema.ResOpenAIChatCompletion)
async def chat_completion(params: OpenAISchema.ReqChatCompletion):
    try:
        messages = [
            {"role": "system", "content": params.sys_prompt},
            {"role": "user", "content": params.user_prompt},
        ]

        res: OpenAISchema.ResOpenAIChatCompletion = openai.chat_completion(
            messages=messages,
            temperature=params.temperature,
            model=params.model,
        )

        return res

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/models", include_in_schema=False)
async def get_models():
    try:
        return openai.get_models_id()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
