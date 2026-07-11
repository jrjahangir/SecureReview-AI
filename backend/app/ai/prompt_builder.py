def build_prompt(source_code: str):

    prompt = f"""
You are a Senior Application Security Engineer.

Review the following source code.

Identify:

1. SQL Injection
2. XSS
3. Hardcoded Secrets
4. Authentication Issues
5. Authorization Issues
6. Weak Cryptography
7. Input Validation Problems
8. OWASP Top 10 Risks

Return your findings as concise bullet points.

Source Code:

{source_code}
"""

    return prompt