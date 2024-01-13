from pydantic import BaseModel


class TokenModel(BaseModel):
    access_token: str
    token_type: str


def to_token_model(token: str) -> TokenModel:
    return TokenModel(access_token=token, token_type="bearer")
