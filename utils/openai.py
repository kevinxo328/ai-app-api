from typing import Union

import openai
from azure.identity import DefaultAzureCredential
from azure.mgmt.cognitiveservices import CognitiveServicesManagementClient

import schemas.openai as OpenAISchema
import utils.env as env

openai.api_type = env.OPENAI_API_TYPE
openai.api_base = env.OPENAI_API_ENDPOINT
openai.api_key = env.OPENAI_API_KEY
openai.api_version = env.OPENAI_API_VERSION


def get_models_id():
    if openai.api_type == "azure":
        client = CognitiveServicesManagementClient(
            credential=DefaultAzureCredential(),
            subscription_id=env.AZURE_OPENAI_SUBSCRIPTION_ID,
        )

        response = client.deployments.list(
            resource_group_name=env.AZURE_OPENAI_RG,
            account_name=env.AZURE_OPENAI_NAME,
        )

        return list(
            {
                "deployment_id": item.name,
                "model": item.properties.model.name,
            }
            for item in response
        )
    else:
        return list(
            {
                "deployment_id": item["id"],
                "model": item["id"],
            }
            for item in openai.Model().list()["data"]
        )


def chat_completion(
    messages: list,
    model: str = env.GPT35_MODEL,
    temperature: Union[int, float] = 0,
) -> OpenAISchema.ChatCompletion:
    openai_chat_completion = openai.ChatCompletion.create(
        engine=model, messages=messages, temperature=temperature
    )

    res = {
        "res": openai_chat_completion,
        "content": openai_chat_completion["choices"][0]["message"]["content"],
    }

    return OpenAISchema.ChatCompletion(**res).model_dump()
