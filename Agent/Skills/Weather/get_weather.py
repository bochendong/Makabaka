import subprocess
import webbrowser
from ...Utils.Utils import get_os

def open_weather_app():
    if (get_os() == "macOS"):
        subprocess.run(["open", "-a", "Weather"])
    else:
        search_url = f"https://www.theweathernetwork.com"
        webbrowser.open(search_url)
