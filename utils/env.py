from pydantic_settings import BaseSettings

# 用 pydantic 管理 env https://myapollo.com.tw/blog/python-pydantic/
# https://docs.pydantic.dev/latest/concepts/pydantic_settings/


class Env(BaseSettings):
    OPENAI_API_TYPE: str = "azure"
    OPENAI_API_VERSION: str = "2023-11-01"
    OPENAI_API_KEY: str
    OPENAI_API_ENDPOINT: str
    GPT35_MODEL: str = "gpt-35-turbo"
    GPT4_MODEL: str = "gpt-4"
    EMBEDDING_MODEL: str = "text-embedding-ada-002"
    AZURE_OPENAI_RG: str
    AZURE_OPENAI_NAME: str
    AZURE_OPENAI_SUBSCRIPTION_ID: str
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    REDIS_USER: str
    REDIS_PASSWORD: str
    SQLALCHEMY_DATABASE_URL: str
    JWT_ALGORITHM: str = "HS256"
    JWT_SECRET_KEY: str = "secret"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 1440

    class Config:
        env_file = ".env"


env = Env()
