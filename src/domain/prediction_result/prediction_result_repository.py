from abc import ABC, abstractmethod
from typing import Optional

from src.domain.prediction_result import prediction_result


class PredictionResultRepository(ABC):
    @abstractmethod
    def insert(self, prediction_result: prediction_result.PredictionResult) -> None:
        raise NotImplementedError

    @abstractmethod
    def fetch_by_user_id(self, user_id: str, limit: int) -> Optional[list[prediction_result.PredictionResult]]:
        raise NotImplementedError
