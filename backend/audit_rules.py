def content_volume_health(subscribers, videos):
    """
    Evaluates content volume vs subscriber traction.
    Returns a dictionary with status and message.
    """

    subscribers = int(subscribers)
    videos = int(videos)

    if videos > 100 and subscribers < 1000:
        return {
            "status": "Weak traction",
            "message": (
                "You have published many videos, but subscriber growth is still low. "
                "This usually means the content topic or presentation lacks clarity. "
                "Try focusing on one clear niche and improving titles and thumbnails."
            )
        }

    elif videos < 50 and subscribers > 5000:
        return {
            "status": "Strong traction",
            "message": (
                "Your channel has gained good subscribers with relatively few videos. "
                "This is a strong sign of content quality and niche clarity. "
                "Stay consistent and build on what is already working."
            )
        }

    else:
        return {
            "status": "Average",
            "message": (
                "Your channel shows average traction based on content volume. "
                "Consistency, clearer positioning, and better presentation "
                "can help improve growth over time."
            )
        }
from datetime import datetime

def upload_consistency(published_at, total_videos):
    """
    Evaluates upload consistency based on channel age and total videos.
    """

    published_date = datetime.strptime(
        published_at, "%Y-%m-%dT%H:%M:%SZ"
    )
    today = datetime.utcnow()

    channel_age_years = max(
        (today - published_date).days / 365, 0.1
    )

    videos_per_year = total_videos / channel_age_years

    if videos_per_year < 6:
        return {
            "status": "Inconsistent",
            "message": (
                "The channel has been active for a long time but uploads are very infrequent. "
                "Long gaps between uploads make it harder for viewers to stay connected."
            )
        }

    elif videos_per_year <= 24:
        return {
            "status": "Moderate",
            "message": (
                "Uploads are somewhat consistent, but increasing frequency could help "
                "build stronger audience engagement over time."
            )
        }

    else:
        return {
            "status": "Consistent",
            "message": (
                "The channel shows strong upload consistency. "
                "Regular publishing helps build trust with viewers and the platform."
            )
        }
def subscriber_video_efficiency(subscribers, total_videos):
    """
    Evaluates how efficiently videos convert into subscribers.
    """

    subscribers = int(subscribers)
    total_videos = int(total_videos)

    if total_videos == 0:
        return {
            "status": "No data",
            "message": "The channel does not have any videos yet."
        }

    ratio = subscribers / total_videos

    if ratio < 10:
        return {
            "status": "Weak conversion",
            "message": (
                "Each video is bringing very few subscribers on average. "
                "This usually indicates unclear content positioning or low viewer retention. "
                "Improving content focus and viewer value can help."
            )
        }

    elif ratio <= 100:
        return {
            "status": "Average conversion",
            "message": (
                "Your videos convert viewers into subscribers at an average rate. "
                "Better hooks, clearer value, and consistent themes can improve this further."
            )
        }

    else:
        return {
            "status": "Strong conversion",
            "message": (
                "Your videos convert viewers into subscribers very effectively. "
                "This is a strong signal of content quality and audience trust."
            )
        }
