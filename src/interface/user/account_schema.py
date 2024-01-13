from pydantic import BaseModel


class UserModel(BaseModel):
    username: str


class SignUpModel(BaseModel):
    username: str
    password: str
