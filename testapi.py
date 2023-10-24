import requests

api_key = "AIzaSyBmEf-CevRAfLfIBM9BMs6mnBuZb0uoUic"

url = "https://maps.googleapis.com/maps/api/geocode/json"

params = {
    "address": "1600 Amphitheatre Parkway, Mountain View, CA",
    "key": api_key
}

response = requests.get(url, params=params)

if response.status_code == 200:
    print("API key is valid!")
else:
    print("API key is invalid.")