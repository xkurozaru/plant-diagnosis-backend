from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from src.domain.prediction_model import prediction_model
from src.infrastructure.common import utils
from src.infrastructure.common.base_model import BaseModel


class PredictionModelEntity(BaseModel):
    __tablename__ = "prediction_model_entities"

    name: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    model_type: Mapped[str] = mapped_column(String(255), nullable=False)
    symptoms: Mapped[str] = mapped_column(Text, nullable=False)
    path: Mapped[str] = mapped_column(Text, nullable=False)

    def to_model(self) -> prediction_model.PredictionModel:
        return prediction_model.recreate_prediction_model(
            self.id,
            self.name,
            self.model_type,
            utils.text_to_list(self.symptoms),
            self.path,
        )


def new_prediction_model_entity(model: prediction_model.PredictionModel) -> PredictionModelEntity:
    return PredictionModelEntity(
        id=model.id,
        name=model.name,
        model_type=model.model_type.value,
        symptoms=utils.list_to_text(model.symptoms),
        path=model.path,
    )
