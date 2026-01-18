from youtube_api import get_channel_basic_stats
from audit_rules import content_volume_health, upload_consistency

data = get_channel_basic_stats("googledevelopers")

if data:
    print("Channel Name:", data["channel_name"])
    print("Subscribers:", data["subscribers"])
    print("Total Views:", data["views"])
    print("Total Videos:", data["videos"])
    print("-" * 40)

    volume_audit = content_volume_health(
        data["subscribers"],
        data["videos"]
    )

    consistency_audit = upload_consistency(
        data["published_at"],
        int(data["videos"])
    )

    print("Content Volume Status:", volume_audit["status"])
    print(volume_audit["message"])
    print("-" * 40)

    print("Upload Consistency Status:", consistency_audit["status"])
    print(consistency_audit["message"])

else:
    print("Channel not found")

from audit_rules import (
    content_volume_health,
    upload_consistency,
    subscriber_video_efficiency
)

print("-" * 40)

efficiency_audit = subscriber_video_efficiency(
    data["subscribers"],
    data["videos"]
)

print("Subscriber Conversion Status:", efficiency_audit["status"])
print(efficiency_audit["message"])

