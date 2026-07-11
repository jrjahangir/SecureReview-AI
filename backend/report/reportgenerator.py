from datetime import datetime

def generate_report(filename, sha256, risk, findings, ai):

    report = {
        "generated_at": datetime.now().isoformat(),
        "filename": filename,
        "sha256": sha256,
        "risk_score": risk["score"],
        "risk_level": risk["level"],
        "summary": risk["summary"],
        "findings": findings,
        "ai_analysis": ai
    }
    return report