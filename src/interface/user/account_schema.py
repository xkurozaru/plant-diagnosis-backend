from pydantic import BaseModel

from src.domain.user.user import User


class UserModel(BaseModel):
    username: str
    role: str


def to_user_model(user: User) -> UserModel:
    return UserModel(
        username=user.username,
        role=user.role.type.value,
    )


class SignUpModel(BaseModel):
    username: str
    password: str
