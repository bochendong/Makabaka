import io
import keyboard
from time import sleep
from queue import Queue
from datetime import datetime
import speech_recognition as sr

from ..Utils.SaveFile import save_audio, save_transcription
from ..IO.Input.VoiceHandler import get_source_recoder, capture_and_save_audio_background
from ..IO.Input.VoiceHandler import is_phrase_complete, speech_to_text
from ..Skills.Action.Action import get_response, MakeAction


def ResponseMode(current_mode):
    print("\n\n####################################################")
    print("Response mode is now activate")
    print("You can press S to Switch to Silence Mode.")

    print("Try ask me the following:")
    print("1. Search python on Google")
    print("2. Play Mozart's music")
    print("3. Show some video of Chinese cuisine")
    print("4. How is the weather tomorrow?")
    print("5. Open Steam")
    print("6. What is the winner of the last world cup?")

    print("Note: Currently some features are only avaliabe on macOS.")

    data_queue = Queue()
    phrase_time = None
    last_sample = bytes()
    source, recorder, record_timeout, phrase_timeout = get_source_recoder()
    capture_and_save_audio_background(data_queue, source, recorder, record_timeout)

    while current_mode["mode"] == "R":
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

                transcription = speech_to_text(file_path)
                save_transcription(transcription, "User")

                response = get_response(transcription, "./Data/Prompt/Decision.txt")
                print(response)
                MakeAction(response, transcription)

                
        except KeyboardInterrupt:
            break

        sleep(0.25)