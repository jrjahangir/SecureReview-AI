import os
import json
from datetime import datetime

from backend.app.report.html_generator import generate_html_report


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

    os.makedirs("backend/reports", exist_ok=True)

    # Save JSON report
    with open(
        "backend/reports/report.json",
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(report, file, indent=4)

    # Generate HTML
    html = generate_html_report(
        filename,
        sha256,
        risk,
        findings,
        ai
    )

    # Save HTML report
    with open(
        "backend/reports/report.html",
        "w",
        encoding="utf-8"
    ) as file:

        file.write(html)

    return report