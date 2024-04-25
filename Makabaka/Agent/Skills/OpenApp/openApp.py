
import os
from ...Utils.Utils import openai_settings, get_prompt
import subprocess

client = openai_settings()

def get_app_to_open(request, appliaction_list, prompt_path):
    rtn = ""
    prompt = get_prompt(prompt_path)
    prompt += "Here is user's application list:\n"
    prompt += appliaction_list + '\n'
    prompt += "Here is the user's request:\n"
    
    try:
        response = client.chat.completions.create(
            messages=[
                {"role": "user", "content": prompt + request }
            ],
            model = "gpt-4-1106-preview"
        )
        rtn = response.choices[0].message.content
    except Exception as e:
        print(f"An Error occurred: {e}")

    return rtn

def list_applications():
    system_apps_dir = '/Applications'
    user_apps_dir = os.path.expanduser('~/Applications')
    macOS_apps_dir = '/System/Applications'
    
    system_apps = [app for app in os.listdir(system_apps_dir) if app.endswith('.app')]
    user_apps = [app for app in os.listdir(user_apps_dir) if app.endswith('.app')]
    OS_apps = [app for app in os.listdir(macOS_apps_dir) if app.endswith('.app')]
    
    all_apps = sorted(set(system_apps + user_apps + OS_apps))
    
    return all_apps

def open_app(keyword):
    all_apps = str(list_applications())
    response = get_app_to_open(keyword, all_apps, './Agent/Prompt/GetAppToOpen.txt')
    response = response.strip("\"'")
    print(response)
    subprocess.run(["open", "-a", response])
