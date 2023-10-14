import os

from dotenv import load_dotenv

load_dotenv(override=True)

OPENAI_API_TYPE = os.environ.get("OPENAI_API_TYPE")
OPENAI_API_VERSION = os.environ.get("OPENAI_API_VERSION")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
OPENAI_API_ENDPOINT = os.environ.get("OPENAI_API_ENDPOINT")

GPT35_TURBO_COMPLETIONS_MODEL = os.environ.get(
    "GPT35_TURBO_COMPLETIONS_MODEL", "gpt-35-turbo"
)
GPT35_TURBO_COMPLETIONS_MODEL_NAME = os.environ.get(
    "GPT35_TURBO_COMPLETIONS_MODEL_NAME", "gpt-35-turbo"
)

EMBEDDING_MODEL = os.environ.get("EMBEDDING_MODEL", "text-embedding-ada-002")
EMBEDDING_MODEL_NAME = os.environ.get("EMBEDDING_MODEL_NAME", "text-embedding-ada-002")
