from backend.app.analyzer.rules.sql_rule import check_sql_injection
from backend.app.analyzer.rules.password_rule import check_password_exposure
from backend.app.analyzer.rules.secret_rule import check_hardcoded_secret
from backend.app.analyzer.rules.crypto_rule import check_weak_crypto

def analyze_source_code(source_code):

    findings = []

    findings.extend(check_sql_injection(source_code))
    findings.extend(check_password_exposure(source_code))
    findings.extend(check_hardcoded_secret(source_code))
    findings.extend(check_weak_crypto(source_code))

    return findings