import urllib.parse
import re

def preprocess_payload(payload: str) -> str:
    
    if not payload:
        return ""

    # URL decode
    payload = urllib.parse.unquote(payload)

    # Convert to lowercase
    payload = payload.lower()

    # Remove extra whitespace
    payload = re.sub(r"\s+", " ", payload)

    # Strip leading and trailing spaces
    payload = payload.strip()

    return payload
