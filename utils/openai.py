from typing import Union

import openai
from azure.identity import DefaultAzureCredential
from azure.mgmt.cognitiveservices import CognitiveServicesManagementClient

import schemas.openai as OpenAISchema
from utils.env import env

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
                "version": item.properties.model.version,
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
    messages: list[dict[str, str]],
    model: str = env.GPT35_MODEL,
    temperature: Union[int, float] = 0,
    stream: bool = False,
) -> OpenAISchema.ResOpenAIChatCompletion:
    openai_chat_completion = openai.ChatCompletion.create(
        engine=model, messages=messages, temperature=temperature, stream=stream
    )

    return openai_chat_completion


def chat_completion_generator(res_openai_stream):
    for chunk in res_openai_stream:
        if "content" in chunk["choices"][0].delta:
            current_response = chunk["choices"][0].delta.content
            yield "data: " + current_response + "\n\n"
