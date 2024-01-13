from torch import nn

from src.domain.common import nano_id
from src.domain.prediction_model import model_type
from src.pytorch.cnn import resnet18


class PredictionModel:
    __id: str
    __name: str
    __model_type: model_type.ModelType
    __symptoms: list[str]
    __path: str

    def __init__(self, id: str, name: str, model_type: model_type.ModelType, symptoms: list[str], path: str) -> None:
        self.__id = id
        self.__name = name
        self.__model_type = model_type
        self.__symptoms = symptoms
        self.__path = path

    @property
    def id(self) -> str:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def model_type(self) -> model_type.ModelType:
        return self.__model_type

    @property
    def symptoms(self) -> list[str]:
        return self.__symptoms

    @property
    def path(self) -> str:
        return self.__path

    def load(self) -> nn.Module:
        if self.model_type == model_type.ModelType.RESNET18:
            return resnet18.ResNet18(len(self.symptoms))
        else:
            raise ValueError(f"Invalid model type: {self.model_type}")

    def idx2symptom(self, idx: int) -> str:
        return self.symptoms[idx]


def new_prediction_model(name: str, type: str, symptoms: list[str], path: str) -> PredictionModel:
    return PredictionModel(
        nano_id.new_nano_id(),
        name,
        model_type.recreate_model_type(type),
        symptoms,
        path,
    )


def recreate_prediction_model(id: str, name: str, type: str, symptoms: list[str], path: str) -> PredictionModel:
    return PredictionModel(
        id,
        name,
        model_type.recreate_model_type(type),
        symptoms,
        path,
    )
