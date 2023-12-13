#!/bin/bash

OPENAI_API_TYPE="azure"
OPENAI_API_VERSION="2023-05-15"
OPENAI_API_KEY=""
OPENAI_API_ENDPOINT=""
GPT35_MODEL="gpt-35-turbo"
GPT4_MODEL="gpt4"
EMBEDDING_MODEL="text-embedding-ada-002"


# Build Docker image
docker build \
			--build-arg OPENAI_API_TYPE=$OPENAI_API_TYPE\
			--build-arg OPENAI_API_VERSION=$OPENAI_API_VERSION\
			--build-arg OPENAI_API_KEY=$OPENAI_API_KEY\
			--build-arg OPENAI_API_ENDPOINT=$OPENAI_API_ENDPOINT\
			--build-arg GPT35_MODEL=$GPT35_MODEL\
			--build-arg GPT4_MODEL=$GPT4_MODEL\
			--build-arg EMBEDDING_MODEL=$EMBEDDING_MODEL\
			-t ai-api .

docker run -d --name ai-api -p 8000:8000 --rm ai-api
