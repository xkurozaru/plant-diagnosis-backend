from pydantic import BaseModel


class SignUpModel(BaseModel):
    username: str
    password: str
