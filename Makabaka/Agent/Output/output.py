import io
from pydub import AudioSegment
from pydub.playback import play
from ..Utils.Utils import openai_settings

client = openai_settings()

def text_to_speech(text):
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text
    )

    byte_stream = io.BytesIO(response.content)

    audio = AudioSegment.from_file(byte_stream, format = "mp3")

    play(audio)
