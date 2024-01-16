from typing import Literal, Optional

from pydantic import BaseModel


class AccessTokenModel(BaseModel):
    client_id: str
    user_id: Optional[str]
    permissions: dict[str, Literal['*'] | list[str]]


class ScopeModel(BaseModel):
    id: str
    type: str
