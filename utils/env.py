import os

from dotenv import load_dotenv

load_dotenv(override=True)

# TODO: 用 pydantic 管理 env https://myapollo.com.tw/blog/python-pydantic/

OPENAI_API_TYPE = os.environ.get("OPENAI_API_TYPE", "")
OPENAI_API_VERSION = os.environ.get("OPENAI_API_VERSION", "")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")
OPENAI_API_ENDPOINT = os.environ.get("OPENAI_API_ENDPOINT", "")

GPT35_MODEL = os.environ.get("GPT35_MODEL", "gpt-35-turbo")
GPT4_MODEL = os.environ.get("GPT4_MODEL", "gpt-4")
EMBEDDING_MODEL = os.environ.get("EMBEDDING_MODEL", "text-embedding-ada-002")

AZURE_OPENAI_RG = os.environ.get("AZURE_OPENAI_RG", "")
AZURE_OPENAI_NAME = os.environ.get("AZURE_OPENAI_NAME", "")
AZURE_OPENAI_SUBSCRIPTION_ID = os.environ.get("AZURE_OPENAI_SUBSCRIPTION_ID", "")
