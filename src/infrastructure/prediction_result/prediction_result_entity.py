from datetime import datetime

from sqlalchemy import DateTime, String
from sqlalchemy.orm import Mapped, mapped_column

from src.domain.prediction_result import prediction_result
from src.infrastructure.common.base_model import BaseModel


class PredictionResultEntity(BaseModel):
    __tablename__ = "prediction_result_entities"

    result: Mapped[str] = mapped_column(String(255), nullable=False)
    predict_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    prediction_model_name: Mapped[str] = mapped_column(String(255), nullable=False)
    user_id: Mapped[str] = mapped_column(String(21), index=True, nullable=False)

    def to_model(self) -> prediction_result.PredictionResult:
        return prediction_result.recreate_prediction_result(
            self.id,
            self.result,
            self.predict_at,
            self.prediction_model_name,
            self.user_id,
        )


def new_prediction_result_entity(result: prediction_result.PredictionResult) -> PredictionResultEntity:
    return PredictionResultEntity(
        id=result.id,
        result=result.result,
        predict_at=result.predict_at,
        prediction_model_name=result.prediction_model_name,
        user_id=result.user_id,
    )
