# Audit Rules v1
# Status: Frozen
# Any new rules must go into v2

from datetime import datetime

def content_volume_health(subscribers, videos):
    """
    Evaluates content volume vs subscriber traction.
    Returns a simple status and mentor-style message.
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
                "Improving consistency, positioning, and presentation "
                "can help improve growth over time."
            )
        }
    
    from datetime import datetime

def upload_consistency(videos, published_at):
    """
    Evaluates how consistent the channel is based on age vs total videos.
    """

    videos = int(videos)

    channel_start = datetime.strptime(
        published_at, "%Y-%m-%dT%H:%M:%SZ"
    )
    today = datetime.utcnow()

    years_active = max((today - channel_start).days / 365, 1)
    videos_per_year = videos / years_active

    if videos_per_year < 12:
        return {
            "status": "Inconsistent",
            "message": (
                "This channel uploads very infrequently for its age. "
                "Long gaps between uploads can slow growth and reduce audience trust."
            )
        }

    elif videos_per_year < 50:
        return {
            "status": "Moderate",
            "message": (
                "This channel uploads occasionally but could benefit from more consistency. "
                "A predictable schedule helps viewers return regularly."
            )
        }

    else:
        return {
            "status": "Consistent",
            "message": (
                "This channel shows good upload consistency for its age. "
                "Maintaining this rhythm supports long-term growth."
            )
        }
    
def subscriber_conversion_efficiency(subscribers, videos):
    """
    Evaluates how effectively videos convert viewers into subscribers.
    """

    subscribers = int(subscribers)
    videos = int(videos)

    if videos == 0:
        return {
            "status": "Not enough data",
            "message": "This channel does not have enough videos to evaluate conversion efficiency."
        }

    subs_per_video = subscribers / videos

    if subs_per_video < 10:
        return {
            "status": "Low conversion",
            "message": (
                "Your videos are attracting views, but relatively few viewers are subscribing. "
                "This may indicate unclear value proposition or weak call-to-action."
            )
        }

    elif subs_per_video < 50:
        return {
            "status": "Average conversion",
            "message": (
                "Your channel shows average subscriber conversion per video. "
                "Improving content hooks and consistency can improve this over time."
            )
        }

    else:
        return {
            "status": "Strong conversion",
            "message": (
                "Your videos convert viewers into subscribers very effectively. "
                "This is a strong indicator of content quality and audience trust."
            )
        }
   

