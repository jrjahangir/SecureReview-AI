import re
def check_weak_crypto(source_code):
    
    findings = []
    
    if re.search(r"\bMD5\b", source_code, re.IGNORECASE):
        findings.append({
          "severity": "Medium",
          "type": "Weak Cryptography",
          "recommendation": "Use SHA-256 or stronger hashing algorithms."
        })
    return findings