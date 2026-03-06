from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from detection.detector import analyze_request
from explainability.explain import generate_evidence

app = FastAPI(
    title="Cartier WAF",
    description="Explainable Web Attack Detection System",
    version="1.0.0"
)

class RequestPayload(BaseModel):
    payload: str

@app.get("/")
def root():
    return {
        "message": "Cartier WAF is running",
        "status": "active"
    }

@app.post("/analyze")
def analyze(payload: RequestPayload):
    try:
        result = analyze_request(payload.payload)
        evidence = generate_evidence(payload.payload)

        response = {
            "payload": payload.payload,
            "attack_type": result.get("attack"),
            "confidence": result.get("confidence"),
            "evidence": evidence,
            "status": "blocked" if result.get("attack") != "Benign" else "allowed"
        }

        return response

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health_check():
    return {
        "service": "Cartier WAF",
        "status": "healthy"
    }
