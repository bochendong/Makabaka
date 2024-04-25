import os
import openai
from openai import OpenAI

def openai_settings():
    openai.api_key = os.environ["OPENAI_API_KEY"]
    client = OpenAI(
        api_key = openai.api_key
    )

    return client

def get_prompt(prompt_path):
    prompt = ""
    with open(prompt_path, "r") as prompt_path:
        for line in prompt_path:
            prompt += line

    return prompt
