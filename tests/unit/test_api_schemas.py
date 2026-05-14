from api.schemas import PredictionRequest, PredictionResponse


def test_prediction_request_default_fields():
    payload = PredictionRequest()
    assert payload.sk_id_curr is None
    assert payload.payload_path is None


def test_prediction_response_creation():
    resp = PredictionResponse(model_name="m", model_version="1", score=0.5, risk_bucket="medium")
    assert resp.model_name == "m"
    assert resp.model_version == "1"
    assert resp.score == 0.5
    assert resp.risk_bucket == "medium"
