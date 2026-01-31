from datetime import datetime, timezone


def posting_consistency_score(last_post_date: str):
    last_post = datetime.fromisoformat(last_post_date.replace("Z", "+00:00"))
    days_gap = (datetime.now(timezone.utc) - last_post).days

    if days_gap <= 3:
        score = 25
    elif days_gap <= 7:
        score = 20
    elif days_gap <= 14:
        score = 15
    elif days_gap <= 30:
        score = 10
    else:
        score = 0

    return {"score": score, "days_gap": days_gap}


def content_activity_score(posts_last_30_days: int):
    if posts_last_30_days >= 15:
        score = 20
    elif posts_last_30_days >= 10:
        score = 16
    elif posts_last_30_days >= 6:
        score = 12
    elif posts_last_30_days >= 3:
        score = 6
    else:
        score = 0

    return {"score": score, "posts_last_30_days": posts_last_30_days}


def content_type_mix_score(content_types: list):
    weights = {"reel": 10, "image": 8, "post": 5, "text": 2}
    score = sum(weights.get(t, 0) for t in set(content_types))

    return {"score": score, "max_score": 25, "types": content_types}


def engagement_health_score(likes: int, comments: int, shares: int):
    if likes and comments and shares:
        score = 25
    elif likes and comments:
        score = 18
    elif likes:
        score = 10
    else:
        score = 0

    return {"score": score}


def final_facebook_audit_result(**metrics):
    total_score = sum(m["score"] for m in metrics.values())

    if total_score >= 90:
        grade = "Excellent"
    elif total_score >= 80:
        grade = "Very Good"
    elif total_score >= 65:
        grade = "Good"
    elif total_score >= 50:
        grade = "Average"
    else:
        grade = "Needs Work"

    return {
        "total_score": total_score,
        "grade": grade,
        "breakdown": metrics
    }
