from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str
    expires: int


class TokenPayload(BaseModel):
    sub: int | str | None = None
