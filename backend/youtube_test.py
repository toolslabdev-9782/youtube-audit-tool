import requests

API_KEY = "AIzaSyC8f2dJZQ1GhqEyzqnQvL2-_SGKN7RKG8w"

url = "https://www.googleapis.com/youtube/v3/channels"

params = {
    "part": "snippet,statistics",
    "forHandle": "googledevelopers",
    "key": API_KEY
}

response = requests.get(url, params=params)
data = response.json()

channel = data["items"][0]

print("Channel Name:", channel["snippet"]["title"])
print("Subscribers:", channel["statistics"]["subscriberCount"])
print("Total Views:", channel["statistics"]["viewCount"])
print("Total Videos:", channel["statistics"]["videoCount"])
