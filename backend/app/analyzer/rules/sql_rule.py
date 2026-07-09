import re

def check_sql_injection(source_code):

    findings = []

    if re.search(r"\bSELECT\b", source_code, re.IGNORECASE):

        findings.append({
            "severity": "High",
            "type": "Potential SQL Injection",
            "recommendation": "Use parameterized queries."
        })
    return findings