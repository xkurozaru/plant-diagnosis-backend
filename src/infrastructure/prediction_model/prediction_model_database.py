from typing import Optional

from sqlalchemy.orm.session import Session

from src.domain.prediction_model import prediction_model, prediction_model_repository
from src.infrastructure.prediction_model import prediction_model_entity


class PredictionModelDatabase(prediction_model_repository.PredictionModelRepository):
    def __init__(self, session: Session) -> None:
        self.__session: Session = session

    def insert(self, model: prediction_model.PredictionModel) -> None:
        try:
            model_e = prediction_model_entity.new_prediction_model_entity(model)
            self.__session.add(model_e)
            self.__session.commit()
        except Exception as e:
            self.__session.rollback()
            raise e

    def fetch_all(self) -> Optional[list[prediction_model.PredictionModel]]:
        try:
            model_es = self.__session.query(prediction_model_entity.PredictionModelEntity).all()
            return [model_e.to_model() for model_e in model_es]
        except Exception as e:
            raise e

    def find_by_id(self, id: str) -> Optional[prediction_model.PredictionModel]:
        try:
            model_e = self.__session.query(prediction_model_entity.PredictionModelEntity).filter_by(id=id).first()
            return model_e.to_model()
        except Exception as e:
            raise e

    def delete(self, model: prediction_model.PredictionModel) -> None:
        try:
            model_e = prediction_model_entity.new_prediction_model_entity(model)
            self.__session.delete(model_e)
            self.__session.commit()
        except Exception as e:
            self.__session.rollback()
            raise e
