from ...Utils.Utils import list_applications, get_os
from ...Utils.ReadSettings import openai_settings, get_prompt
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
            model = "gpt-4o"
        )
        rtn = response.choices[0].message.content
    except Exception as e:
        print(f"An Error occurred: {e}")

    return rtn


def open_app(keyword):
    if (get_os() == "macOS"):
        all_apps = str(list_applications())
        response = get_app_to_open(keyword, all_apps, './Agent/Prompt/GetAppToOpen.txt')
        response = response.strip("\"'")
        subprocess.run(["open", "-a", response])
    else:
        print("We are not able to open an application on Windows currently")