from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException
from youtube_api import get_channel_basic_stats
from audit_rules import (
    content_volume_health,
    upload_consistency,
    subscriber_conversion_efficiency
)

app = FastAPI(title="YouTube Channel Audit API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://audit.techinyourlife.com",
        "http://localhost",
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "YouTube Audit API is running"}

@app.get("/audit")
def audit_channel(channel: str):
    data = get_channel_basic_stats(channel)

    if not data:
        raise HTTPException(status_code=404, detail="Channel not found")

    audit_1 = content_volume_health(
        data["subscribers"],
        data["videos"]
    )

    audit_2 = upload_consistency(
        data["videos"],
        data["published_at"]
    )

    audit_3 = subscriber_conversion_efficiency(
        data["subscribers"],
        data["videos"]
    )

    return {
        "success": True,
        "channel": {
            "name": data["channel_name"],
            "subscribers": data["subscribers"],
            "views": data["views"],
            "videos": data["videos"],
            "created": data["published_at"]
        },
        "audits": {
            "content_volume_health": audit_1,
            "upload_consistency": audit_2,
            "subscriber_conversion_efficiency": audit_3
        }
    }
