from abc import ABC, abstractmethod
from typing import Optional

from src.domain.prediction_model import prediction_model


class PredictionModelRepository(ABC):
    @abstractmethod
    def insert(self, prediction_model: prediction_model.PredictionModel) -> None:
        raise NotImplementedError

    @abstractmethod
    def fetch_all(self) -> Optional[list[prediction_model.PredictionModel]]:
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, id: str) -> Optional[prediction_model.PredictionModel]:
        raise NotImplementedError

    @abstractmethod
    def delete(self, prediction_model: prediction_model.PredictionModel) -> None:
        raise NotImplementedError
