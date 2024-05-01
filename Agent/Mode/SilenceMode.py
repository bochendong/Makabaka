import io
from time import sleep
from queue import Queue
from datetime import datetime
import speech_recognition as sr

from ..Utils.SaveFile import save_audio, save_transcription
from ..IO.Input.VoiceHandler import get_source_recoder, capture_and_save_audio_background
from ..IO.Input.VoiceHandler import is_phrase_complete, speech_to_text

def SilenceMode(current_mode):
    print("\n\n####################################################")
    print("Silence mode is now activate")
    print("You can press R to Switch to Response Mode.")
    data_queue = Queue()
    phrase_time = None
    last_sample = bytes()
    source, recorder, record_timeout, phrase_timeout = get_source_recoder()
    capture_and_save_audio_background(data_queue, source, recorder, record_timeout)

    while current_mode["mode"] == "S":
        now = datetime.utcnow()
        try:
            if not data_queue.empty():
                if is_phrase_complete(phrase_time, phrase_timeout):
                    last_sample = bytes()
                
                phrase_time = now

                while not data_queue.empty():
                    data = data_queue.get()
                    last_sample += data
                
                audio_data = sr.AudioData(last_sample, source.SAMPLE_RATE, source.SAMPLE_WIDTH)
                wav_data = io.BytesIO(audio_data.get_wav_data())
                file_path = save_audio(wav_data)
                print(file_path)

                transcription = speech_to_text(file_path)
                save_transcription(transcription, "User")
                
        except KeyboardInterrupt:
            break

        sleep(0.25)
    