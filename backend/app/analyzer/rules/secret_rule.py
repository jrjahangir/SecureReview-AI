import re
def check_hardcoded_secret(source_code):

    findings = []
 # Hardcoded Secret
    if re.search(r"\b(api_key|secret)\b", source_code, re.IGNORECASE):
        findings.append({
            "severity": "High",
            "type": "Hardcoded Secret",
            "recommendation": "Store secrets securely using environment variables or a secrets manager."
        })   
    return findings