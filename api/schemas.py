from pydantic import BaseModel
from typing import Optional


class PredictionRequest(BaseModel):
    sk_id_curr: Optional[int] = None
    payload_path: Optional[str] = None


class PredictionResponse(BaseModel):
    model_name: str
    model_version: str
    score: Optional[float] = None
    risk_bucket: Optional[str] = None
