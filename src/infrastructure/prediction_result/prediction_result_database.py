from typing import Optional

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

    def fetch_by_user_id(self, user_id: str, limit=10) -> Optional[list[prediction_result.PredictionResult]]:
        try:
            result_es = (
                self.session.query(prediction_result_entity.PredictionResultEntity)
                .filter(prediction_result_entity.PredictionResultEntity.user_id == user_id)
                .order_by(prediction_result_entity.PredictionResultEntity.predict_at.desc())
                .limit(limit)
                .all()
            )
            return [result_e.to_model() for result_e in result_es]
        except Exception as e:
            self.session.rollback()
            raise e
