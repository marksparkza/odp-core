from typing import Optional

from pydantic import BaseModel, Field


class UserModel(BaseModel):
    id: str
    email: str
    active: bool
    verified: bool
    name: str
    picture: Optional[str]
    role_ids: list[str]
    provider_keys: dict[str, str] = Field(..., title='Provider id:key pairs')


class UserModelIn(BaseModel):
    id: str
    active: bool
    role_ids: list[str]
