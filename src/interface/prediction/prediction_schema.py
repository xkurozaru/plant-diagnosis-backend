from pydantic import BaseModel

from src.domain.prediction_model.prediction_model import PredictionModel
from src.domain.prediction_result.prediction_result import PredictionResult


class PredictionModelModel(BaseModel):
    id: str
    name: str
    symptoms: list[str]


def to_prediction_model_model(prediction_model: PredictionModel) -> PredictionModelModel:
    return PredictionModelModel(
        id=prediction_model.id,
        name=prediction_model.name,
        symptoms=prediction_model.symptoms,
    )


def to_prediction_models_model(prediction_models: list[PredictionModel]) -> list[PredictionModelModel]:
    return [to_prediction_model_model(prediction_model) for prediction_model in prediction_models]


class PredictionResultModel(BaseModel):
    id: str
    result: str
    predict_at: str
    prediction_model_name: str


def to_prediction_result_model(prediction_result: PredictionResult) -> PredictionResultModel:
    return PredictionResultModel(
        id=prediction_result.id,
        result=prediction_result.result,
        predict_at=prediction_result.predict_at.strftime("%Y-%m-%d %H:%M:%S"),
        prediction_model_name=prediction_result.prediction_model_name,
    )


def to_prediction_results_model(prediction_results: list[PredictionResult]) -> list[PredictionResultModel]:
    return [to_prediction_result_model(prediction_result) for prediction_result in prediction_results]


class CreatePredictionModelModel(BaseModel):
    name: str
    type: str
    symptoms: list[str]
    path: str
