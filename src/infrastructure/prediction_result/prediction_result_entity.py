from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.domain.prediction_result import prediction_result
from src.infrastructure.common.base_model import BaseModel


class PredictionResultEntity(BaseModel):
    __tablename__ = "prediction_result_entities"

    result: Mapped[str] = mapped_column(String(255), nullable=False)
    prediction_model_id: Mapped[str] = mapped_column(String(21), nullable=False)
    user_id: Mapped[str] = mapped_column(String(21), index=True, nullable=False)

    def to_model(self) -> prediction_result.PredictionResult:
        return prediction_result.recreate_prediction_result(
            self.id,
            self.result,
            self.prediction_model_id,
            self.user_id,
        )


def new_prediction_result_entity(result: prediction_result.PredictionResult) -> PredictionResultEntity:
    return PredictionResultEntity(
        id=result.id,
        result=result.result,
        prediction_model_id=result.prediction_model_id,
        user_id=result.user_id,
    )
