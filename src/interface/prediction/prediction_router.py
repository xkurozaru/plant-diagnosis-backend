from fastapi import APIRouter, Depends, HTTPException, UploadFile, status
from PIL import Image
from sqlalchemy.orm import Session

from src.application.prediction_application_service import PredictionApplicationService
from src.domain.prediction_result.prediction_service import PredictionService
from src.infrastructure.database import get_db
from src.infrastructure.prediction_model.prediction_model_database import PredictionModelDatabase
from src.infrastructure.prediction_result.prediction_result_database import PredictionResultDatabase
from src.infrastructure.user.user_database import UserDatabase
from src.interface.common.authorization import authorize
from src.interface.prediction import prediction_schema

router = APIRouter()


def get_prediction_application_service(db: Session = Depends(get_db)) -> PredictionApplicationService:
    return PredictionApplicationService(
        UserDatabase(db),
        PredictionModelDatabase(db),
        PredictionResultDatabase(db),
        PredictionService(),
    )


@router.get("/api/prediction-models", response_model=list[prediction_schema.PredictionModelModel])
def get_prediction_models(
    user_id=Depends(authorize),
    prediction_application_service: PredictionApplicationService = Depends(get_prediction_application_service),
):
    try:
        return prediction_application_service.get_prediction_models(user_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.post("/api/prediction-models")
def create_prediction_model(
    data: prediction_schema.CreatePredictionModelModel,
    user_id=Depends(authorize),
    prediction_application_service: PredictionApplicationService = Depends(get_prediction_application_service),
):
    try:
        prediction_application_service.create_prediction_model(user_id, data.name, data.type, data.symptoms, data.path)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.delete("/api/prediction-models/{id}")
def delete_prediction_model(
    id: str,
    user_id=Depends(authorize),
    prediction_application_service: PredictionApplicationService = Depends(get_prediction_application_service),
):
    try:
        prediction_application_service.delete_prediction_model(user_id, id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.get("/api/prediction-results", response_model=list[prediction_schema.PredictionResultModel])
def get_prediction_results(
    user_id=Depends(authorize),
    prediction_application_service: PredictionApplicationService = Depends(get_prediction_application_service),
):
    try:
        return prediction_application_service.get_prediction_results(user_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.post("/api/prediction-models/{id}")
def predict(
    id: str,
    image_file: UploadFile,
    user_id=Depends(authorize),
    prediction_application_service: PredictionApplicationService = Depends(get_prediction_application_service),
):
    try:
        image = Image.open(image_file.file)
        prediction_application_service.predict(
            user_id,
            id,
            image,
        )
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    finally:
        image_file.file.close()
