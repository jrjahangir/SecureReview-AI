def calculate_risk(findings):

    score = 0
    counts = {
        "Critical": 0,
        "High": 0,
        "Medium": 0,
        "Low": 0
    }

    for finding in findings:

        severity = finding["severity"]

        counts[severity] += 1

        if severity == "Critical":
            score += 50

        elif severity == "High":
            score += 30

        elif severity == "Medium":
            score += 15

        elif severity == "Low":
            score += 5

    # Cap the score at 100
    score = min(score, 100)

    if score >= 90:
        level = "Very Critical"

    elif score >= 80:
        level = "Critical"

    elif score >= 60:
        level = "High"

    elif score >= 30:
        level = "Medium"

    else:
        level = "Low"

    return {
        "score": score,
        "level": level,
        "summary": counts
    }