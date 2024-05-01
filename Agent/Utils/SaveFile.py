import os
from .ReadSettings import read_user_settings
from datetime import datetime

def save_audio(wav_data):
    current_time = datetime.now().strftime("%Y%m%d%H%M%S")

    dir_path = "./Data/audio/" + current_time[:-6]

    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    file_name = f"{current_time}.wav"

    file_path = os.path.join(dir_path, file_name)

    with open(file_path, 'w+b') as f:
        f.write(wav_data.read())
    
    print("Save audio at" + current_time)

    return file_path

def save_transcription(transcription, type = "User"):
    data = read_user_settings()
    current_time = datetime.now().strftime("%Y%m%d%H%M%S")

    dir_path = "./Data/transcription/" + current_time[:-6]

    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    
    file_name = f"daily_record.txt"
    file_path = os.path.join(dir_path, file_name)

    f = open(file_path, "a")
    if (type == "User"):
        f.write(f'[{current_time}]: ({data["Username"]}) {transcription} \n')
    else:
        f.write(f'[{current_time}]: (Makabaka) {transcription} \n')
    f.close()