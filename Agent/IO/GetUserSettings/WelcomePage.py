from ..Output.Text2Speech import text_to_speech_local, text_to_speech
from ..Input.VoiceHandler import capture_and_save_audio
from ...Utils.ReadSettings import read_user_settings, create_data_folder


import json

def welcome_page():
    print(r"""
     __  __       _         _      _            _    
    |  \/  | __ _| | __ ___| | __ | |__      __| |  __
    | |\/| |/ _` | |/ / _` | |/ / | | _  \  / _` | / /
    | |  | | (_) |   < (_) |   <  | | (_) || (_) |  < 
    |_|  |_|\__,_|_|\_\__,_|_|\_\ |_|__, /  \__,_| \_\
                                                
    """)

    print("\n----------------------------------------------------------------\n")


    create_data_folder()
    data = read_user_settings()

    if (data["Username"] == "None"):
        user_name = input("What is your name?\n")
        data["Username"] = user_name
        print("\n----------------------------------------------------------------\n")
    
    if (data["UserLanguage"] == "None"):
        user_language = input("What is your prefered language?\nType en for English, zh-cn for Chinese.\n")
        if (user_language == "en" or user_language == "zh-cn"):
            data["UserLanguage"] = user_language
        else:
            print("Unsupported language detected, will use Chinese for default User Language")
            data["UserLanguage"] = "zh-cn"
        
        print("\n----------------------------------------------------------------\n")
            
    if (data["VoiceSettings"] == "None"):
        print("Do you want me to use your voice as output? [y/n]")
        print("Note:")
        print("If 'n' was entered, we will use openai's text to speech api (Fast but Cost Money)")
        print("Else the text to speech will run on local device (Slow but Free)")
        print("\n")
        print("We Recommand to enter 'n' if your device does not support GPU.")
        print("\n")
        voice_settings = input("Enter your input: \n")

        if (voice_settings.lower() == "n"):
            data["VoiceSettings"] = "Default"

            text_to_speech("你好，我是玛卡巴卡，很高兴成为你的私人助理。")
        else :
            data["VoiceSettings"] = "User Voice"

            print("Please read the following:\n")

            if (data["UserLanguage"] == "zh-cn"):
                print("你好玛卡巴卡，很期待与你的相遇，作为我的私人助理，你需要帮我搜索信息，打开应用，查看天气，观看视频，规划行程，记录我的日常信息。")
            else:
                print("Hello, glad to meet you. As my personal assistant, you need to help me search for information, open apps, check the weather, watch videos, plan trips, and record my daily information.")
            
            temp = input("Hit enter to Record your Voice\n")

            capture_and_save_audio(f'./Data/SampleVoice/{data["Username"]}')

            print("Analysing your voice ...")

            text_to_speech_local("你好，我是玛卡巴卡，很高兴成为你的私人助理。", data["UserLanguage"],
                                 input_path = f'./Data/SampleVoice/{data["Username"]}/sample_1.wav', 
                                 output_path = f"./Data/Temp/output.wav")

            print("\n----------------------------------------------------------------\n")

    
    file_path = './Data/Settings/User.json'
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

    print("I'm currently support two mode\n1. Silence Mode: Will listen at background and record your life\n")
    print("2. Response Mode: Will handle your request.\n")
    print("The default mode is Silence Mode.")
    user_input = input("Hit Enter to continue ...\n")

