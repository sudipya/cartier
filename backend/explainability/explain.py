def generate_evidence(payload: str):

    payload = payload.lower()
    evidence = []

    if "<script" in payload:
        evidence.append("Script tag detected (possible XSS)")

    if "javascript:" in payload:
        evidence.append("JavaScript protocol usage detected")

    if "onerror=" in payload or "onload=" in payload:
        evidence.append("Suspicious HTML event handler detected")

    if " or 1=1" in payload or "' or '" in payload:
        evidence.append("SQL logical condition detected")

    if "union select" in payload:
        evidence.append("SQL UNION SELECT pattern detected")

    if "127.0.0.1" in payload or "localhost" in payload:
        evidence.append("Localhost access attempt (possible SSRF)")

    if "169.254.169.254" in payload:
        evidence.append("Cloud metadata endpoint access detected")

    if ";" in payload:
        evidence.append("Command separator detected (possible RCE)")

    if "|" in payload or "&&" in payload:
        evidence.append("Command chaining detected")

    if not evidence:
        evidence.append("No obvious attack signature detected")

    return evidence
