from fastapi import FastAPI
from api.schemas import PredictionRequest, PredictionResponse

app = FastAPI(title="Credit Risk API", version="0.1.0")


@app.get('/health')
def health() -> dict:
    return {"status": "ok"}


@app.get('/model-info')
def model_info() -> dict:
    return {"model_name": "credit_default_model", "stage": "staging", "note": "placeholder"}


@app.post('/predict', response_model=PredictionResponse)
def predict(request: PredictionRequest) -> PredictionResponse:
    return PredictionResponse(model_name="credit_default_model", model_version="0", score=None, risk_bucket=None)
