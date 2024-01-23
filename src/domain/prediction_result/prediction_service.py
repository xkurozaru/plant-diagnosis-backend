import torch
from PIL import Image
from torch import Tensor
from torchvision.transforms import v2

from src.domain.prediction_model.prediction_model import PredictionModel
from src.domain.prediction_result.prediction_result import PredictionResult, new_prediction_result
from src.domain.user.user import User


class PredictionService:
    def __init__(self) -> None:
        pass

    def predict(self, user: User, model: PredictionModel, image: Image) -> PredictionResult:
        cnn = model.load()
        cnn.load_state_dict(torch.load(model.path, map_location=torch.device("cpu")))
        cnn.eval()

        image_tensor = self.image_transform(image)
        with torch.inference_mode():
            output = cnn(image_tensor)

        _, pred = output.max(1)
        result = model.idx2symptom(pred.item())

        del cnn, image_tensor, output, pred

        return new_prediction_result(result, model.name, user.id)

    def image_transform(self, image: Image) -> Tensor:
        transforms = v2.Compose(
            [
                v2.ToImage(),
                v2.Resize((224, 224)),
                v2.ToDtype(torch.float32, scale=True),
                v2.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
            ]
        )
        return transforms(image).unsqueeze(0)
