import os
import openai
from openai import OpenAI

from ...Utils.ReadSettings import read_user_settings, get_prompt
from ...Utils.SaveFile import save_transcription
from ...IO.Output.Text2Speech import text_to_speech, text_to_speech_local, play_wav_file
from ..Chrome.browser_on_chrome import search_on_chrome
from ..MusicBrowser.browser_on_youtube import search_music_on_youtube
from ..VideoBrowser.browser_on_youtube import search_video_on_youtube
from ..OpenApp.open_app import open_app
from ..Weather.get_weather import open_weather_app

openai.api_key = os.environ["OPENAI_API_KEY"]
client = OpenAI(
    api_key = openai.api_key
)

def get_response(request, prompt_path):
    rtn = ""
    prompt = get_prompt(prompt_path)
    try:
        response = client.chat.completions.create(
            messages=[
                {"role": "user", "content": prompt + request }
            ],
            model = "gpt-4-1106-preview"
        )
        rtn = response.choices[0].message.content
    except Exception as e:
        print(f"An Error occurred: {e}")

    return rtn

def get_app_to_open(request, appliaction_list, prompt_path):
    rtn = ""
    prompt = get_prompt(prompt_path)
    prompt += "Here is user's application list:\n"
    prompt += appliaction_list + '\n'
    prompt += "Here is the user's request:\n"
    
    try:
        response = client.chat.completions.create(
            messages=[
                {"role": "user", "content": prompt + request }
            ],
            model = "gpt-4-1106-preview"
        )
        rtn = response.choices[0].message.content
    except Exception as e:
        print(f"An Error occurred: {e}")

    return rtn

def MakeAction(response, transcription):
    data = read_user_settings()
    action, keyword = response.split("|")
    action = action.lower().strip(" \"'`")

    if (action == "search on google"):
        search_on_chrome(keyword)
    elif (action == "play music"):
        search_music_on_youtube(keyword)
    elif (action == "show video"):
        search_video_on_youtube(keyword)
    elif (action == "direct response"):
        save_transcription(keyword, 'System')
        if (data["VoiceSettings"] == "Default"):
            text_to_speech(keyword)
        else:
            print("Due to Running on Local Device and No GPU Support")
            print("The text to speech is quite slow now.")

            text_to_speech_local(keyword, data["UserLanguage"],
                                 input_path = f'./Data/Voice_sample/{data["Username"]}/sample_1.wav', 
                                 output_path = f"./Data/Temp/output.wav")
            play_wav_file("./Data/Temp/output.wav")
    elif (action == "open application"):
        try:
            open_app(transcription)
        except:
            print("There was an error detected to open the app.")
    elif (action.lower().strip() == "check weather"):
        open_weather_app()
    else:
        print("I cannot handle this request")