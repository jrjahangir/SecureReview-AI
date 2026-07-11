def build_prompt(source_code: str):

    return f"""
You are a Senior Application Security Engineer.

Review the following source code.

Return ONLY valid JSON.

Use exactly this format:

{{
  "overall_risk": "",
  "issues":[
    {{
      "severity":"",
      "type":"",
      "cwe":"",
      "owasp":"",
      "recommendation":""
    }}
  ]
}}

Rules:

- No markdown
- No explanations outside JSON
- Return valid JSON only
- If no issue exists, return an empty issues array.

Source Code:

{source_code}
"""