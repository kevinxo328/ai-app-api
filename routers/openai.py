import json

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse

import schemas.openai as OpenAISchema
import security.oauth2 as oauth2_security
import utils.openai as openai
import utils.redis as redis_utils
from schemas.user import User

router = APIRouter(
    prefix="/openai",
    tags=["openai"],
    dependencies=[Depends(oauth2_security.get_current_active_user)],
)


# TODO: Global Exception https://stackoverflow.com/questions/61596911/catch-exception-globally-in-fastapi
@router.post("/chat_completion", response_model=OpenAISchema.ResOpenAIChatCompletion)
async def chat_completion(
    params: OpenAISchema.ReqChatCompletion,
    user: User = Depends(oauth2_security.get_current_active_user),
):
    MEMORY_EXPIRE = 60 * 10
    MEMORY_MAX_ROUND = 5 * 2
    try:
        memory = redis_utils.redis_client.hget(user.username, "chat_completion")
        memory_list = []
        if memory is not None:
            if isinstance(memory, bytes):
                memory_list = json.loads(memory.decode("utf-8"))

        messages = [
            {
                "role": "system",
                "content": params.sys_prompt
                + f"Chat History: {json.dumps(memory_list)}",
            },
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

        memory_list.append(
            {"role": "user", "content": params.user_prompt},
        )
        memory_list.append(
            {"role": "openai", "content": res.choices[0]["message"]["content"]},
        )

        if len(memory_list) > MEMORY_MAX_ROUND:
            memory_list = memory_list[-MEMORY_MAX_ROUND:]

        redis_utils.redis_client.hset(
            user.username,
            "chat_completion",
            json.dumps(memory_list),
        )

        redis_utils.redis_client.expire(user.username, MEMORY_EXPIRE)
        return res

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/models")
async def get_models():
    try:
        return openai.get_models_id()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
