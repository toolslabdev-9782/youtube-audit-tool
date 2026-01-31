import os
import requests

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

YOUTUBE_SEARCH_URL = "https://www.googleapis.com/youtube/v3/search"
YOUTUBE_CHANNEL_URL = "https://www.googleapis.com/youtube/v3/channels"


def get_channel_data(query: str):
    if not YOUTUBE_API_KEY:
        return None

    # STEP 1: Search channel (most reliable)
    search_response = requests.get(
        YOUTUBE_SEARCH_URL,
        params={
            "part": "snippet",
            "q": query,
            "type": "channel",
            "maxResults": 1,
            "key": YOUTUBE_API_KEY
        },
        timeout=10
    ).json()

    if not search_response.get("items"):
        return None

    channel_id = search_response["items"][0]["snippet"]["channelId"]

    # STEP 2: Fetch channel stats by ID
    channel_response = requests.get(
        YOUTUBE_CHANNEL_URL,
        params={
            "part": "snippet,statistics",
            "id": channel_id,
            "key": YOUTUBE_API_KEY
        },
        timeout=10
    ).json()

    if not channel_response.get("items"):
        return None

    return channel_response["items"][0]
