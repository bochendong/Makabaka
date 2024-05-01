
# A new method to record voice


import speech_recognition as sr
import os
from datetime import datetime
import openai
from openai import OpenAI


from Agent.Mode.ResponseMode import ResponseMode
from Agent.Mode.SilenceMode import SilenceMode
from Agent.IO.GetUserSettings.WelcomePage import welcome_page
import threading

welcome_page()
current_mode = {"mode": "S"}

def input_handler():
    global current_mode
    while current_mode["mode"] != "Q":
        user_input = input().upper()
        if user_input in ["R", "S", "Q"]:
            current_mode["mode"] = user_input
        else:
            print("INVALID INPUT. Please enter 'R' for Response Mode, 'S' for Silence Mode, or 'Q' to quit.")

def mode_manager():
    while current_mode["mode"] != "Q":
        if current_mode["mode"] == "R":
            print("\n\nActivating Response Mode ... ")
            ResponseMode(current_mode)
        elif current_mode["mode"] == "S":
            print("\n\nActivating Silence Mode ... ")
            SilenceMode(current_mode)

if __name__ == "__main__":
    input_thread = threading.Thread(target=input_handler)
    mode_thread = threading.Thread(target=mode_manager)

    input_thread.start()
    mode_thread.start()

    input_thread.join()
    mode_thread.join()

'''
recognizer = sr.Recognizer()
recognizer.pause_threshold = 0.6


openai.api_key = os.environ["OPENAI_API_KEY"]
client = OpenAI(
        api_key = openai.api_key
    )


def get_source_recoder():
    record_timeout = 2
    phrase_timeout = 3

    recorder = sr.Recognizer()
    recognizer.pause_threshold = 0.6
    recorder.energy_threshold = 1000
    recorder.dynamic_energy_threshold = False
    source = sr.Microphone(sample_rate=16000)

    return source, recorder, record_timeout, phrase_timeout

def capture_and_save_audio_background(data_queue, source, recorder, record_timeout):
    with source:
        recorder.adjust_for_ambient_noise(source)

    def record_callback(_, audio:sr.AudioData) -> None:
        data = audio.get_raw_data()
        data_queue.put(data)

    print("Recorder start Listening at backend")
    recorder.listen_in_background(source, record_callback, phrase_time_limit=record_timeout)


def speech_to_text(file_path):
    with open(file_path, 'rb') as audio_file:
        # Assuming 'client' is previously defined and authenticated
        transcription = client.audio.transcriptions.create(
            model="whisper-1", 
            file=audio_file,
            response_format='text'
        )
    return transcription
'''




'''
while(True):
    with sr.Microphone() as source:
        print("去除背景噪音中...")
        recognizer.adjust_for_ambient_noise(source)

        print("生成文件名...")
        file_path = "./Data/audio"
        current_time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = f"{current_time}.wav"
        file_path = os.path.join(file_path, file_name)

        print("录制中...")
        try:
            audio_data = recognizer.listen(source, timeout= 5)

            with open(file_path, 'wb') as file:
                file.write(audio_data.get_wav_data())
            
            print(f"Audio saved to {file_path}")
        except Exception as e:
            print(f"Error: {e}")

    print("Generating Transcription")
    with open(file_path, "rb") as audio_file:
            transcription = client.audio.transcriptions.create(
                model = "whisper-1",
                file = audio_file,
                response_format = 'text'
            )
        
    file_name = "daily_record.txt"
    transcript_path = "./data/Transcripts"

    file_path = os.path.join(transcript_path, file_name)
        
    f = open(file_path, 'a')

    print("Saving Transcription")

    f.write(f'[{current_time}]: {transcription}')

    f.close()
'''        






'''
import sounddevice as sd
from scipy.io.wavfile import write

def voice_handler():
    duration = 10
    fs = 44100

    print("Recording for", duration, "seconds ...")

    recording = sd.rec(int (duration * fs), samplerate = fs, channels = 1, dtype = 'float64')
    sd.wait()

    if not os.path.exists("./data/user_sample_voice"):
        os.makedirs("./data/user_sample_voice")

    file_name = f"Nancy_voice.wav"
    file_path = os.path.join("./data/user_sample_voice", file_name)

    write(file_path, fs, recording)

# "你好，作为我的私人助理，你需要帮我搜索信息，打开应用，查看天气，观看视频，记录我的日常信息"

voice_handler()
'''

'''
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
'''

