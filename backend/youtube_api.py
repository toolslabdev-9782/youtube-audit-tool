import requests

API_KEY = "AIzaSyC8f2dJZQ1GhqEyzqnQvL2-_SGKN7RKG8w"

def get_channel_basic_stats(channel_handle):
    url = "https://www.googleapis.com/youtube/v3/channels"
    
    params = {
        "part": "snippet,statistics",
        "forHandle": channel_handle,
        "key": API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    if "items" not in data or len(data["items"]) == 0:
        return None

    item = data["items"][0]

    return {
    "channel_name": item["snippet"]["title"],
    "subscribers": item["statistics"]["subscriberCount"],
    "views": item["statistics"]["viewCount"],
    "videos": item["statistics"]["videoCount"],
    "published_at": item["snippet"]["publishedAt"]
}

