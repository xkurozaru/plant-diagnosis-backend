from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from src.application.account_application_service import AccountApplicationService
from src.infrastructure.database import get_db
from src.infrastructure.user.user_database import UserDatabase
from src.interface.common import common_schema
from src.interface.common.authorization import authorize, generate_token
from src.interface.user import account_schema

router = APIRouter()


def get_account_application_service(db: Session = Depends(get_db)) -> AccountApplicationService:
    return AccountApplicationService(
        UserDatabase(db),
    )


@router.post("/api/sign-up")
def sign_up(
    data: account_schema.SignUpModel,
    account_application_service: AccountApplicationService = Depends(get_account_application_service),
):
    try:
        user = account_application_service.sign_up(data.username, data.password)
        token = generate_token(user.id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    return common_schema.to_token_model(token)


@router.post("/api/sign-up/admin")
def sign_up_admin(
    data: account_schema.SignUpModel,
    account_application_service: AccountApplicationService = Depends(get_account_application_service),
):
    try:
        user = account_application_service.sign_up_admin(data.username, data.password)
        token = generate_token(user.id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    return common_schema.to_token_model(token)


@router.post("/api/sign-in")
def sign_in(
    data: Annotated[OAuth2PasswordRequestForm, Depends()],
    account_application_service: AccountApplicationService = Depends(get_account_application_service),
) -> common_schema.TokenModel:
    try:
        user = account_application_service.sign_in(data.username, data.password)
        token = generate_token(user.id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    return common_schema.to_token_model(token)


@router.get("/api/users/me")
def get_user(
    user_id: str = Depends(authorize),
    account_application_service: AccountApplicationService = Depends(get_account_application_service),
) -> account_schema.UserModel:
    try:
        user = account_application_service.get_user(user_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    return account_schema.to_user_model(user)
