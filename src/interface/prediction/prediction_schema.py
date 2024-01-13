from pydantic import BaseModel


class PredictionModelModel(BaseModel):
    id: str
    name: str
    symptoms: list[str]


class PredictionResultModel(BaseModel):
    result: str
    predict_at: str
    prediction_model_name: str


class CreatePredictionModelModel(BaseModel):
    name: str
    type: str
    symptoms: list[str]
    path: str
