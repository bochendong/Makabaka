import sounddevice as sd
import os
from scipy.io.wavfile import write
from datetime import datetime
import openai
from openai import OpenAI

openai.api_key = os.environ["OPENAI_API_KEY"]
client = OpenAI(
    api_key = openai.api_key
)

AUDIO_PATH = '../Data/audio'

def voice_handler():
    duration = 5
    fs = 44100

    print("Recording for", duration, "seconds ...")

    recording = sd.rec(int (duration * fs), samplerate = fs, channels = 1, dtype = 'float64')
    sd.wait()

    print("Recording finished")

    current_time = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = f"{current_time}.wav"
    file_path = os.path.join(AUDIO_PATH, file_name)

    write(file_path, fs, recording)

    print("Audio saved to " + file_path)

    with open(file_path, 'rb') as audio_file:
        transcription = client.audio.transcriptions.create(
            model="whisper-1", 
            file=audio_file,
            response_format= 'text'
        )
    return transcription


print(voice_handler())

