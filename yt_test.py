from youtube_api import get_channel_basic_stats
from audit_rules import (
    content_volume_health,
    upload_consistency,
    subscriber_conversion_efficiency
)

data = get_channel_basic_stats("googledevelopers")

if data:
    print("Channel Name:", data["channel_name"])
    print("Subscribers:", data["subscribers"])
    print("Total Views:", data["views"])
    print("Total Videos:", data["videos"])
    print("Channel Created:", data["published_at"])

    print("\n" + "-" * 40)

    audit1 = content_volume_health(
        data["subscribers"],
        data["videos"]
    )

    audit2 = upload_consistency(
        data["videos"],
        data["published_at"]
    )

    audit3 = subscriber_conversion_efficiency(
        data["subscribers"],
        data["videos"]
    )

    print("Audit 1 — Content Volume Health")
    print("Status:", audit1["status"])
    print("Message:", audit1["message"])

    print("\nAudit 2 — Upload Consistency")
    print("Status:", audit2["status"])
    print("Message:", audit2["message"])

    print("\nAudit 3 — Subscriber Conversion Efficiency")
    print("Status:", audit3["status"])
    print("Message:", audit3["message"])

else:
    print("Channel not found")
