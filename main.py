import os
import openai
from openai import OpenAI

from Agent.Input.Voice_handler import voice_handler
from Agent.Output.output import text_to_speech

openai.api_key = os.environ["OPENAI_API_KEY"]
client = OpenAI(
    api_key = openai.api_key
)

def get_response(prompt):
    rtn = ""

    try:
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are Trump." },
                {"role": "user", "content": prompt }
            ],

            model = "gpt-4-1106-preview"
        )
        rtn = response.choices[0].message.content
    except Exception as e:
        print(f"An Error occurred: {e}")

    return rtn


input = voice_handler()
response = get_response(input)
text_to_speech(response)
