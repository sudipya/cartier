from fastapi import APIRouter, HTTPException
from database.models import AnalyzeRequest, AnalyzeResponse
from detection.detector import analyze_request
from explainability.explain import generate_evidence
from database.db import db

router = APIRouter()

@router.get("/")
def root():
    return {"message": "Cartier WAF API running"}

@router.post("/analyze", response_model=AnalyzeResponse)
def analyze(req: AnalyzeRequest):
    try:
        result = analyze_request(req.payload)
        evidence = generate_evidence(req.payload)

        status = "blocked" if result["attack"] != "Benign" else "allowed"

        db.log_attack(
            payload=req.payload,
            attack_type=result["attack"],
            confidence=result["confidence"],
            evidence=evidence
        )

        return AnalyzeResponse(
            payload=req.payload,
            attack_type=result["attack"],
            confidence=result["confidence"],
            evidence=evidence,
            status=status
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/logs")
def get_logs():
    return db.get_logs()
