from pydantic import BaseModel


class PredictionModelModel(BaseModel):
    id: str
    name: str
    symptoms: list[str]


class CreatePredictionModelModel(BaseModel):
    name: str
    type: str
    symptoms: list[str]
    path: str
