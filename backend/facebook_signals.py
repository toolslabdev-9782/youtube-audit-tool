from datetime import datetime, timedelta
import hashlib


def extract_facebook_signals(page_input: str):
    """
    Deterministic fake signals
    Same page → same result
    Different page → different result
    """

    seed = int(hashlib.md5(page_input.lower().encode()).hexdigest(), 16)

    posts_last_30_days = (seed % 18) + 4
    likes = (seed % 300) + 30
    comments = (seed % 60) + 4
    shares = (seed % 40) + 1

    days_gap = seed % 15
    last_post_date = (
        datetime.utcnow() - timedelta(days=days_gap)
    ).strftime("%Y-%m-%dT%H:%M:%SZ")

    content_pool = ["reel", "image", "post", "text"]
    content_types = content_pool[: (seed % 4) + 1]

    return {
        "last_post_date": last_post_date,
        "posts_last_30_days": posts_last_30_days,
        "content_types": content_types,
        "likes": likes,
        "comments": comments,
        "shares": shares
    }
