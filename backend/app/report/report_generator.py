import os
import json
from datetime import datetime

from backend.app.report.html_generator import generate_html_report
from backend.app.report.file_naming import generate_report_filename


def generate_report(
    filename,
    sha256,
    risk,
    findings,
    ai
):
    """
    Generate JSON and HTML security assessment reports.
    """

    # Create reports directory if it does not exist
    os.makedirs("backend/reports", exist_ok=True)

    # Generate unique filenames
    json_filename = generate_report_filename(
        filename,
        "json"
    )

    html_filename = generate_report_filename(
        filename,
        "html"
    )

    # Full file paths
    json_path = os.path.join(
        "backend",
        "reports",
        json_filename
    )

    html_path = os.path.join(
        "backend",
        "reports",
        html_filename
    )

    # Build report dictionary
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

    # Save JSON report
    with open(
        json_path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            report,
            file,
            indent=4
        )

    # Generate HTML report
    html = generate_html_report(
        filename,
        sha256,
        risk,
        findings,
        ai
    )

    # Save HTML report
    with open(
        html_path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(html)

    # Return report with generated file locations
    report["json_report"] = json_path
    report["html_report"] = html_path

    return report