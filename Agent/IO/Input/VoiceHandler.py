import os
from datetime import datetime
import speech_recognition as sr
from datetime import datetime, timedelta
from ...Utils.ReadSettings import openai_settings, read_voice_settings

client = openai_settings()

AUDIO_PATH = './Data/audio'

if not os.path.exists(AUDIO_PATH):
    os.makedirs(AUDIO_PATH)

def capture_and_save_audio(save_path = './Data/audio'):
    """
    Captures audio from the microphone and saves it as a WAV file.

    This function adjusts for ambient noise, listens for audio, and saves
    the detected audio to a WAV file named with the current timestamp.

    Returns:
        str: The path to the saved audio file.
    """

    recognizer = sr.Recognizer()
    recognizer.pause_threshold = 1
    with sr.Microphone() as source:
        print("Adjusting for ambient noise, please wait...")
        recognizer.adjust_for_ambient_noise(source)

        if not os.path.exists(save_path):
            os.makedirs(save_path)


        current_time = datetime.now().strftime("%Y%m%d%H%M%S")
        
        if (save_path == AUDIO_PATH):
            file_name = f"{current_time}.wav"
        else:
            file_name = f"sample_1.wav"
            
        file_path = os.path.join(save_path, file_name)

        print("Listening...")
        try:
            audio_data = recognizer.listen(source, timeout=5)
            with open(file_path, "wb") as file:
                file.write(audio_data.get_wav_data())
            print(f"Audio saved to {file_path}")
        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for phrase to start.")
        except Exception as e:
            print(f"Error: {e}")

    return file_path

def is_phrase_complete(phrase_time, phrase_timeout):
    now = datetime.utcnow()
    return phrase_time and now - phrase_time > timedelta(seconds=phrase_timeout)

def get_source_recoder():
    data = read_voice_settings()
    record_timeout = data['record_timeout']
    phrase_timeout = data['phrase_timeout']
    recorder = sr.Recognizer()
    recorder.energy_threshold = data['energy_threshold']
    recorder.dynamic_energy_threshold = data['dynamic_energy_threshold']
    source = sr.Microphone(sample_rate=data['sample_rate'])

    return source, recorder, record_timeout, phrase_timeout

def capture_and_save_audio_background(data_queue, source, recorder, record_timeout):
    with source:
        recorder.adjust_for_ambient_noise(source)

    def record_callback(_, audio:sr.AudioData) -> None:
        """
        Threaded callback function to recieve audio data when recordings finish.
        audio: An AudioData containing the recorded bytes.
        """
        data = audio.get_raw_data()
        data_queue.put(data)

    print("Recorder start Listening at backend")
    recorder.listen_in_background(source, record_callback, phrase_time_limit=record_timeout)


def speech_to_text(file_path):
    """
    Converts speech in an audio file to text using a transcription service.

    Args:
        file_path (str): The path to the audio file to be transcribed.

    Returns:
        The transcription of the audio file.
    """
    with open(file_path, 'rb') as audio_file:
        transcription = client.audio.transcriptions.create(
            model="whisper-1", 
            file=audio_file,
            response_format='text'
        )
    return transcription


