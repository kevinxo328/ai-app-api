import redis

from utils.env import env

redis_client = redis.Redis(
    host=env.REDIS_HOST,
    port=env.REDIS_PORT,
    password=env.REDIS_PASSWORD,
    username=env.REDIS_USER,
    ssl=True,
)
