from ...Utils.Utils import get_public_ip, get_os
from geopy.geocoders import Nominatim
import geocoder
import subprocess
import json

def get_location_by_ip():
    public_ip = get_public_ip()

    ip = geocoder.ip(public_ip)

    if ip:
        return (ip.city, ip.latlng)
    else:
        print("Error: Can not get your IP address.")
        return None

def get_location():
    if (get_os() == "macOS"):
        try:
            result = subprocess.run(['CoreLocationCLI', '-format', '%json'], stdout=subprocess.PIPE, text=True)
            if result.stdout:
                location_data = json.loads(result.stdout)
                print(location_data)
            else:
                print("Location could not be determined.")
        except:
            print("Location access denied from your device, we will find location based on IP")
            return get_location_by_ip()

    else:
        print("Do not support location look-up on your device, we will find location based on IP")
        return get_location_by_ip()
    