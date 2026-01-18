from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import requests

from backend.audit_rules import (
    content_volume_health,
    upload_consistency,
    subscriber_video_efficiency
)


API_KEY = "AIzaSyC8f2dJZQ1GhqEyzqnQvL2-_SGKN7RKG8w"

app = FastAPI(
    title="YouTube Channel Audit API",
    description="Free YouTube channel health and audit tool",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "YouTube Audit API is running"}

@app.get("/audit")
def audit_channel(
    channel: str = Query(..., description="YouTube channel handle")
):
    url = "https://www.googleapis.com/youtube/v3/channels"

    params = {
        "part": "snippet,statistics",
        "forHandle": channel,
        "key": API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    if "items" not in data or len(data["items"]) == 0:
        return {
            "success": False,
            "error": "Channel not found"
        }

    item = data["items"][0]

    channel_data = {
        "name": item["snippet"]["title"],
        "subscribers": item["statistics"]["subscriberCount"],
        "views": item["statistics"]["viewCount"],
        "videos": item["statistics"]["videoCount"],
        "published_at": item["snippet"]["publishedAt"]
    }

    audits = {
        "content_volume": content_volume_health(
            channel_data["subscribers"],
            channel_data["videos"]
        ),
        "upload_consistency": upload_consistency(
            channel_data["published_at"],
            int(channel_data["videos"])
        ),
        "subscriber_efficiency": subscriber_video_efficiency(
            channel_data["subscribers"],
            channel_data["videos"]
        )
    }

    return {
        "success": True,
        "channel": channel_data,
        "audits": audits
    }


