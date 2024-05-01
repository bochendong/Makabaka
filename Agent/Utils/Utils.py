import os
import platform
import requests

def get_os():
    os_name = platform.system()
    if os_name == "Darwin":
        return "macOS"
    elif os_name == "Windows":
        return "Windows"
    else:
        return "Unknown"
    
def get_public_ip():
    response = requests.get('https://api.ipify.org')
    if response.status_code == 200:
        return response.text
    else:
        return "Could not fetch IP address"
    
def list_applications():
    system_apps_dir = '/Applications'
    user_apps_dir = os.path.expanduser('~/Applications')
    macOS_apps_dir = '/System/Applications'
    
    system_apps = [app for app in os.listdir(system_apps_dir) if app.endswith('.app')]
    user_apps = [app for app in os.listdir(user_apps_dir) if app.endswith('.app')]
    OS_apps = [app for app in os.listdir(macOS_apps_dir) if app.endswith('.app')]
    
    all_apps = sorted(set(system_apps + user_apps + OS_apps))
    
    return all_apps
