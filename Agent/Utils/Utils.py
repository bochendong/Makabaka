import os
import openai
from openai import OpenAI

def openai_settings():
    openai.api_key = os.environ["OPENAI_API_KEY"]
    client = OpenAI(
        api_key = openai.api_key
    )

    return client
