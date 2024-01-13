from enum import Enum


class ModelType(Enum):
    RESNET18 = "resnet18"


def recreate_model_type(type: str) -> ModelType:
    if type == ModelType.RESNET18.value:
        return ModelType.RESNET18
    else:
        raise ValueError(f"Invalid model type: {type}")
