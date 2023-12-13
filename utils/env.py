import os

from dotenv import load_dotenv

load_dotenv(override=True)

# TODO: 用 pydantic 管理 env https://myapollo.com.tw/blog/python-pydantic/

OPENAI_API_TYPE = os.environ.get("OPENAI_API_TYPE", "azure")
OPENAI_API_VERSION = os.environ.get("OPENAI_API_VERSION", "2023-11-01")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")
OPENAI_API_ENDPOINT = os.environ.get("OPENAI_API_ENDPOINT", "")

GPT35_MODEL = os.environ.get("GPT35_MODEL", "gpt-35-turbo")
GPT4_MODEL = os.environ.get("GPT4_MODEL", "gpt-4")
EMBEDDING_MODEL = os.environ.get("EMBEDDING_MODEL", "text-embedding-ada-002")

AZURE_OPENAI_RG = os.environ.get("AZURE_OPENAI_RG", "")
AZURE_OPENAI_NAME = os.environ.get("AZURE_OPENAI_NAME", "")
AZURE_OPENAI_SUBSCRIPTION_ID = os.environ.get("AZURE_OPENAI_SUBSCRIPTION_ID", "")

REDIS_HOST = os.environ.get("REDIS_HOST", "localhost")
REDIS_PORT = os.environ.get("REDIS_PORT", 6379)
REDIS_USER = os.environ.get("REDIS_USER", "")
REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD", "")
