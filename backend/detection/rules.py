from detection.rules import rule_detection
from detection.ml_model import ml_detection
from detection.preprocess import preprocess_payload

def analyze_request(payload: str):

    clean_payload = preprocess_payload(payload)

    rule_result = rule_detection(clean_payload)

    if rule_result:
        return {
            "attack": rule_result,
            "confidence": 0.95
        }

    ml_result = ml_detection(clean_payload)

    if ml_result and ml_result != "Benign":
        return {
            "attack": ml_result,
            "confidence": 0.85
        }

    return {
        "attack": "Benign",
        "confidence": 0.99
    }
