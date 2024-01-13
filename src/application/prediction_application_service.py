from PIL import Image

from src.domain.prediction_model.prediction_model import PredictionModel, new_prediction_model
from src.domain.prediction_model.prediction_model_repository import PredictionModelRepository
from src.domain.prediction_result.prediction_result import PredictionResult
from src.domain.prediction_result.prediction_result_repository import PredictionResultRepository
from src.domain.prediction_result.prediction_service import PredictionService
from src.domain.user.user_repository import UserRepository


class PredictionApplicationService:
    def __init__(
        self,
        user_repository: UserRepository,
        prediction_model_repository: PredictionModelRepository,
        prediction_result_repository: PredictionResultRepository,
        prediction_service: PredictionService,
    ) -> None:
        self.__user_repository: UserRepository = user_repository
        self.__prediction_model_repository: PredictionModelRepository = prediction_model_repository
        self.__prediction_result_repository: PredictionResultRepository = prediction_result_repository
        self.__prediction_service: PredictionService = prediction_service

    def get_prediction_models(self, user_id) -> list[PredictionModel]:
        user = self.__user_repository.find_by_id(user_id)
        if user is None:
            raise Exception("User not found")

        return self.__prediction_model_repository.fetch_all()

    def create_prediction_model(self, user_id, name: str, type: str, symptoms: list[str], path: str) -> None:
        user = self.__user_repository.find_by_id(user_id)
        if user is None:
            raise Exception("User not found")

        prediction_model = new_prediction_model(name, type, symptoms, path)
        self.__prediction_model_repository.insert(prediction_model)

    def predict(self, user_id, model_id: str, image: Image) -> PredictionResult:
        user = self.__user_repository.find_by_id(user_id)
        if user is None:
            raise Exception("User not found")

        prediction_model = self.__prediction_model_repository.find_by_id(model_id)
        if prediction_model is None:
            raise Exception("Prediction model not found")

        prediction_result = self.__prediction_service.predict(user, prediction_model, image)
        self.__prediction_result_repository.insert(prediction_result)

        return prediction_result

    def delete_prediction_model(self, user_id, id: str) -> None:
        user = self.__user_repository.find_by_id(user_id)
        if user is None:
            raise Exception("User not found")

        prediction_model = self.__prediction_model_repository.find_by_id(id)
        self.__prediction_model_repository.delete(prediction_model)
