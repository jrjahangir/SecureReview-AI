ISSUE_FIELDS = [
    "severity",
    "type",
    "recommendation",
    "cwe",
    "owasp"
]

ALLOWED_RISKS = [
    "Critical",
    "High",
    "Medium",
    "Low",
    "Informational"
]


def validate_issue(issue):

    for field in ISSUE_FIELDS:
        if field not in issue or issue[field] in (None, ""):
            raise ValueError(f"Issue missing field: {field}")

    return issue


def validate_ai_analysis(ai_analysis):

    required_fields = [
        "overall_risk",
        "issues"
    ]

    for field in required_fields:
        if field not in ai_analysis:
            raise ValueError(f"Missing AI field: {field}")

    if not isinstance(ai_analysis["issues"], list):
        raise ValueError("'issues' must be a list")

    overall_risk = ai_analysis["overall_risk"].strip()

    if overall_risk == "":
        raise ValueError("overall_risk cannot be empty")

    if overall_risk not in ALLOWED_RISKS:
        raise ValueError(f"Invalid overall_risk: {overall_risk}")

    for issue in ai_analysis["issues"]:
        validate_issue(issue)

    return ai_analysis