import webbrowser
import urllib.parse

def search_on_chrome(request):
    encoded_query = urllib.parse.quote_plus(request)
    search_url = f'https://www.google.com/search?q={encoded_query}'

    webbrowser.open(search_url)

    print("The website is opened")


