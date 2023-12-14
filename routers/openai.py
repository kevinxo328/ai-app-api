from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse

import schemas.openai as OpenAISchema
import utils.openai as openai

router = APIRouter(prefix="/openai", tags=["openai"])


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
            stream=params.stream,
        )

        if params.stream:
            return StreamingResponse(
                openai.chat_completion_generator(res),
                media_type="text/event-stream",
            )

        return res

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/models")
async def get_models():
    try:
        return openai.get_models_id()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
