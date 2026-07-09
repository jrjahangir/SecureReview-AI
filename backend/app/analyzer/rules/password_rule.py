import re
def check_password_exposure(source_code):

    findings = []

    if re.search(r"\bpassword\b", source_code, re.IGNORECASE):
        findings.append({
            "severity": "Medium",
            "type": "Sensitive Information Exposure",
            "recommendation": "Avoid exposing passwords."
        })
    return findings