from fastapi import FastAPI, HTTPException
from datetime import datetime
from youtube_api import get_channel_data
from audit_rules import (
    channel_health,
    upload_consistency,
    conversion_efficiency
)

app = FastAPI()


@app.get("/")
def home():
    return {"message": "YouTube Audit API is running"}


@app.get("/audit")
def audit_channel(channel: str):
    channel_data = get_channel_data(channel)

    if not channel_data:
        raise HTTPException(status_code=404, detail="Channel not found")

    stats = channel_data["statistics"]
    snippet = channel_data["snippet"]

    subscribers = int(stats.get("subscriberCount", 0))
    views = int(stats.get("viewCount", 0))
    videos = int(stats.get("videoCount", 0))

    published_at = snippet.get("publishedAt")
    years_active = 0
    if published_at:
        years_active = max(
            1,
            datetime.now().year - datetime.fromisoformat(published_at.replace("Z", "")).year
        )

    audits = {
        "channel_health": channel_health(subscribers, videos),
        "upload_consistency": upload_consistency(videos, years_active),
        "conversion_efficiency": conversion_efficiency(subscribers, views)
    }

    return {
        "success": True,
        "channel": {
            "name": snippet.get("title"),
            "subscribers": subscribers,
            "views": views,
            "videos": videos
        },
        "audits": audits
    }
