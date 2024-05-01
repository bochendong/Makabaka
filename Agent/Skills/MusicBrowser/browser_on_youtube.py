
import webbrowser
import urllib.parse

def search_music_on_youtube(request):
    encoded_query = urllib.parse.quote_plus(request)
    
    search_url = f"https://www.youtube.com/results?search_query={encoded_query}"
    
    webbrowser.open(search_url)

    print("The request is already handled.")
