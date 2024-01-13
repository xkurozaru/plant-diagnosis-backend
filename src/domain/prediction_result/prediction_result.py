from datetime import datetime

from src.domain.common import date_time, nano_id


class PredictionResult:
    __id: str
    __result: str
    __predict_at: datetime
    __prediction_model_name: str
    __user_id: str

    def __init__(self, id: str, result: str, predict_at: datetime, prediction_model_name: str, user_id: str) -> None:
        self.__id = id
        self.__result = result
        self.__predict_at = predict_at
        self.__prediction_model_name = prediction_model_name
        self.__user_id = user_id

    @property
    def id(self) -> str:
        return self.__id

    @property
    def result(self) -> str:
        return self.__result

    @property
    def predict_at(self) -> datetime:
        return self.__predict_at

    @property
    def prediction_model_name(self) -> str:
        return self.__prediction_model_name

    @property
    def user_id(self) -> str:
        return self.__user_id


def new_prediction_result(result: str, prediction_model_name: str, user_id: str) -> "PredictionResult":
    return PredictionResult(
        nano_id.new_nano_id(),
        result,
        date_time.date_time_now(),
        prediction_model_name,
        user_id,
    )


def recreate_prediction_result(
    id: str, result: str, predict_at: datetime, prediction_model_name: str, user_id: str
) -> "PredictionResult":
    return PredictionResult(
        id,
        result,
        predict_at,
        prediction_model_name,
        user_id,
    )
