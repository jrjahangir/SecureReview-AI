from datetime import datetime


def generate_html_report(
    filename,
    sha256,
    risk,
    findings,
    ai_result
):

    html = f"""
<!DOCTYPE html>

<html>

<head>

<meta charset="UTF-8">

<title>SecureReview-AI Report</title>

<style>

body {{
    font-family: Arial, Helvetica, sans-serif;
    background: #f5f7fa;
    margin: 30px;
}}

.container {{
    background: white;
    padding: 30px;
    border-radius: 10px;
    box-shadow: 0 0 10px #cccccc;
}}

h1 {{
    color: #0b5394;
}}

h2 {{
    color: #444;
}}

table {{
    width: 100%;
    border-collapse: collapse;
    margin-top: 15px;
    margin-bottom: 20px;
}}

th {{
    background: #0b5394;
    color: white;
    padding: 10px;
}}

td {{
    border: 1px solid #ddd;
    padding: 8px;
}}

.high {{
    color: red;
    font-weight: bold;
}}

.medium {{
    color: orange;
    font-weight: bold;
}}

.low {{
    color: green;
    font-weight: bold;
}}

.critical {{
    color: darkred;
    font-weight: bold;
}}

.info {{
    color: blue;
    font-weight: bold;
}}

.footer {{
    margin-top: 40px;
    padding-top: 15px;
    border-top: 2px solid #0b5394;
    color: #666;
    font-size: 14px;
    text-align: center;
}}

</style>

</head>

<body>

<div class="container">

<h1>SecureReview-AI</h1>

<h2>Security Assessment Report</h2>

<hr>

<h3>General Information</h3>

<p><b>Filename:</b> {filename}</p>

<p><b>Generated:</b> {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>

<p><b>SHA256:</b> {sha256}</p>

<hr>

<h3>Risk Summary</h3>

<table>

<tr>
<th>Risk Score</th>
<th>Risk Level</th>
</tr>

<tr>
<td>{risk["score"]}</td>
<td>{risk["level"]}</td>
</tr>

</table>

<hr>

<h3>Static Analysis Findings</h3>

<table>

<tr>
<th>Severity</th>
<th>Issue</th>
<th>Recommendation</th>
</tr>
"""

    # Static Findings
    for finding in findings:

        severity = finding["severity"]
        css_class = severity.lower()

        html += f"""
<tr>

<td class="{css_class}">
{severity}
</td>

<td>
{finding["type"]}
</td>

<td>
{finding["recommendation"]}
</td>

</tr>
"""

    html += f"""

</table>

<hr>

<h3>AI Analysis</h3>

<p>

<b>Model:</b> {ai_result["model"]}

</p>

<p>

<b>Overall Risk:</b>
{ai_result["analysis"]["overall_risk"]}

</p>

<table>

<tr>

<th>Severity</th>
<th>Issue</th>
<th>CWE</th>
<th>OWASP</th>
<th>Recommendation</th>

</tr>
"""

    # AI Findings
    for issue in ai_result["analysis"]["issues"]:

        severity = issue["severity"]
        css_class = severity.lower()

        html += f"""
<tr>

<td class="{css_class}">
{severity}
</td>

<td>
{issue["type"]}
</td>

<td>
{issue["cwe"]}
</td>

<td>
{issue["owasp"]}
</td>

<td>
{issue["recommendation"]}
</td>

</tr>
"""

    html += f"""

</table>

<div class="footer">

<b>SecureReview-AI</b><br><br>

AI-Powered Static & Intelligent Security Code Review Platform<br><br>

Version: <b>0.1.0</b><br>

Generated:
{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}<br>

AI Model:
<b>{ai_result["model"]}</b><br><br>

Developed by<br>

<b>Md. Jahangir Hossain</b><br>

Information Security Architect<br><br>

© 2026 SecureReview-AI. All Rights Reserved.

</div>

</div>

</body>

</html>
"""

    return html