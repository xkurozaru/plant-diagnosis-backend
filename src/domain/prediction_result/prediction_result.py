from src.domain.common import nano_id


class PredictionResult:
    __id: str
    __result: str
    __prediction_model_id: str
    __user_id: str

    def __init__(self, id: str, result: str, prediction_model_id: str, user_id: str) -> None:
        self.__id = id
        self.__result = result
        self.__prediction_model_id = prediction_model_id
        self.__user_id = user_id

    @property
    def id(self) -> str:
        return self.__id

    @property
    def result(self) -> str:
        return self.__result

    @property
    def prediction_model_id(self) -> str:
        return self.__prediction_model_id

    @property
    def user_id(self) -> str:
        return self.__user_id


def new_prediction_result(result: str, prediction_model_id: str, user_id: str) -> "PredictionResult":
    return PredictionResult(
        nano_id.new_nano_id(),
        result,
        prediction_model_id,
        user_id,
    )


def recreate_prediction_result(id: str, result: str, prediction_model_id: str, user_id: str) -> "PredictionResult":
    return PredictionResult(
        id,
        result,
        prediction_model_id,
        user_id,
    )
