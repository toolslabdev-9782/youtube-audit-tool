def channel_health(subscribers, videos):
    if subscribers < 1000 and videos > 50:
        return {
            "status": "Poor",
            "message": "Many videos but very low subscribers. Content positioning needs improvement."
        }
    elif subscribers < 10000:
        return {
            "status": "Average",
            "message": "Channel is growing slowly. Focus on consistency and topic clarity."
        }
    else:
        return {
            "status": "Good",
            "message": "Healthy subscriber growth relative to content volume."
        }


def upload_consistency(videos, years_active):
    if years_active == 0:
        return {
            "status": "Unknown",
            "message": "Not enough data to judge upload consistency."
        }

    uploads_per_year = videos / years_active

    if uploads_per_year < 12:
        return {
            "status": "Low",
            "message": "Uploads are infrequent. Consider posting more consistently."
        }
    elif uploads_per_year < 50:
        return {
            "status": "Average",
            "message": "Moderate upload frequency. Increasing consistency may help growth."
        }
    else:
        return {
            "status": "Good",
            "message": "Strong upload consistency."
        }


def conversion_efficiency(subscribers, views):
    if views == 0:
        return {
            "status": "Unknown",
            "message": "Not enough views to calculate conversion."
        }

    ratio = subscribers / views

    if ratio < 0.001:
        return {
            "status": "Poor",
            "message": "Low subscriber conversion from views. Improve CTAs and content hooks."
        }
    elif ratio < 0.005:
        return {
            "status": "Average",
            "message": "Decent conversion. There is room for optimization."
        }
    else:
        return {
            "status": "Good",
            "message": "Strong conversion from views to subscribers."
        }
