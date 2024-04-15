import io
import os
from pydub import AudioSegment
from pydub.playback import play
import openai
from openai import OpenAI

openai.api_key = os.environ["OPENAI_API_KEY"]
client = OpenAI(
    api_key = openai.api_key
)

AUDIO_PATH = '../Data/audio'

def text_to_speech(text):
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text
    )

    byte_stream = io.BytesIO(response.content)

    audio = AudioSegment.from_file(byte_stream, format = "mp3")

    play(audio)
    
text_to_speech("你好，主人")
