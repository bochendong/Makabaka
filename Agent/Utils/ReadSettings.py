import os
import openai
import json
from openai import OpenAI

def read_voice_settings():
    file_path = './Data/Settings/Voice.json'
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    return data

def read_user_settings():
    file_path = './Data/Settings/User.json'
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    return data

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
