import io
from pydub import AudioSegment
from pydub.playback import play
from ...Utils.ReadSettings import openai_settings

import pyaudio  
import wave  

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


def text_to_speech_local(text, user_language, input_path, output_path):
    # tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=False)

    # tts.tts_to_file(text=text,
                    #file_path=output_path,
                    #speaker_wav=input_path,
                    #language=user_language)
    pass

def play_wav_file(file_path):
    chunk = 1024  
  
    f = wave.open(file_path,"rb")  
    p = pyaudio.PyAudio()  

    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                    channels = f.getnchannels(),  
                    rate = f.getframerate(),  
                    output = True)  
      
    data = f.readframes(chunk)  
      
    while data:  
        stream.write(data)  
        data = f.readframes(chunk)  
    
    stream.stop_stream()  
    stream.close()  

    p.terminate()  

