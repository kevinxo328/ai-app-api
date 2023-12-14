from fastapi import APIRouter, HTTPException

import utils.redis as redis_utils

router = APIRouter(prefix="/redis", tags=["redis"])


@router.get("/health_check")
async def health_check():
    try:
        return redis_utils.redis_client.ping()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# @router.get("/redis/{key}")
# def get_redis_value(key: str):
#     value = redis_client.get(key)
#     if value is None:
#         return {"message": "Key not found"}
#     return {"key": key, "value": value.decode()}


# @router.post("/redis/{key}")
# def set_redis_value(key: str, value: str):
#     redis_client.set(key, value)
#     return {"message": "Value set successfully"}


# @router.delete("/redis/{key}")
# def delete_redis_value(key: str):
#     deleted = redis_client.delete(key)
#     if deleted == 0:
#         return {"message": "Key not found"}
#     return {"message": "Key deleted successfully"}
