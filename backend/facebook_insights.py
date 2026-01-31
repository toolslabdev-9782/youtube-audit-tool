def generate_insights(breakdown):
    strengths = []
    weaknesses = []
    recommendations = []

    for key, data in breakdown.items():
        score = data.get("score", 0)

        if score >= 15:
            strengths.append(f"{key.replace('_',' ').title()} is strong")
        elif score <= 5:
            weaknesses.append(f"{key.replace('_',' ').title()} is weak")
            recommendations.append(f"Improve {key.replace('_',' ')}")

    return {
        "strengths": strengths,
        "weaknesses": weaknesses,
        "recommendations": recommendations
    }
