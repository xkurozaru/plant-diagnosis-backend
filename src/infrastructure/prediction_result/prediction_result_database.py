from sqlalchemy.orm import Session

from src.domain.prediction_result import prediction_result, prediction_result_repository
from src.infrastructure.prediction_result import prediction_result_entity


class PredictionResultDatabase(prediction_result_repository.PredictionResultRepository):
    def __init__(self, session: Session) -> None:
        self.session = session

    def insert(self, result: prediction_result.PredictionResult) -> None:
        try:
            result_e = prediction_result_entity.new_prediction_result_entity(result)
            self.session.add(result_e)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e

    def delete(self, result: prediction_result.PredictionResult) -> None:
        try:
            result_e = prediction_result_entity.new_prediction_result_entity(result)
            self.session.delete(result_e)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e
