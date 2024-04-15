import io
from pydub import AudioSegment
from pydub.playback import play
import openai
from openai import OpenAI
import os
api_key = os.getenv('OPENAI_API_KEY')
if api_key is None:
    raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")

client = OpenAI(
    api_key = openai.api_key
)

AUDIO_PATH = './Data/audio'

def text_to_speech(text):
    response = client.audio.speech.create(
        model="tts-1",
        voice="nova",
        input=text
    )

    byte_stream = io.BytesIO(response.content)

    audio = AudioSegment.from_file(byte_stream, format = "mp3")

    play(audio)
    
text_to_speech("你好，主人")
