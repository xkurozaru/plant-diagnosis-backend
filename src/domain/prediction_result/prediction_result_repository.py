from abc import ABC, abstractmethod

from src.domain.prediction_result import prediction_result


class PredictionResultRepository(ABC):
    @abstractmethod
    def insert(self, prediction_result: prediction_result.PredictionResult) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, prediction_result: prediction_result.PredictionResult) -> None:
        raise NotImplementedError
