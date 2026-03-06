from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class AttackLog(BaseModel):
    payload: str
    attack_type: str
    confidence: float
    evidence: List[str]
    timestamp: Optional[datetime] = datetime.utcnow()

class AnalyzeRequest(BaseModel):
    payload: str

class AnalyzeResponse(BaseModel):
    payload: str
    attack_type: str
    confidence: float
    evidence: List[str]
    status: str
