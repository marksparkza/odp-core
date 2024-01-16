from typing import Optional

from pydantic import BaseModel


class UserModel(BaseModel):
    id: str
    email: str
    active: bool
    verified: bool
    name: str
    picture: Optional[str]
    role_ids: list[str]


class UserModelIn(BaseModel):
    id: str
    active: bool
    role_ids: list[str]
