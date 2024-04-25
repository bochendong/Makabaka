import os
import openai
from openai import OpenAI

from Agent.Input.Voice_handler import voice_handler
from Agent.Output.output import text_to_speech

from Agent.Skills.Chrome.browser_on_chome import search_on_chrome
from Agent.Skills.MusicBrowser.browser_on_youtube import play_music_on_youtube
from Agent.Skills.Weather.get_weather import open_weather_app
from Agent.Skills.OpenApp.openApp import open_app

openai.api_key = os.environ["OPENAI_API_KEY"]
client = OpenAI(
    api_key = openai.api_key
)

def get_response(request):
    prompt = ""

    with open ('./Agent/Prompt/Decision.txt', 'r') as prompt_path:
        for line in prompt_path:
            prompt += line

    try:
        response = client.chat.completions.create(
            messages=[
                {"role": "user", "content": prompt + request}
            ],

            model = "gpt-4-1106-preview"
        )
        rtn = response.choices[0].message.content
    except Exception as e:
        print(f"An Error occurred: {e}")

    return rtn

user_request = voice_handler()     
response = get_response(user_request)
action, keyword = response.split("|")
action = action.strip(" '\"").lower()
keyword = keyword.strip(" '\"").lower()

if (action == "search on google"):
    search_on_chrome(keyword)  
elif (action == "play music"):
    play_music_on_youtube(keyword)
elif (action == "check weather"):
    open_weather_app()
elif (action == "open application"):
    open_app(keyword)
elif (action == "direct response"):
    print(text_to_speech(keyword))


