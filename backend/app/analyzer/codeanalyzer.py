def analyze_source_code(source_code: str):
    findings = []
    if "SELECT" in source_code.upper():
        findings.append({
            "severity": "High",
            "type": "Potential SQL Injection",
            "recommendation":
                "Use parameterized queries."
        })

    return findings