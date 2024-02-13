from dataclasses import dataclass
from typing import Literal, Optional

from pydantic import BaseModel

Permissions = dict[str, Literal['*'] | list[str]]
"""The effective set of permissions for a user or a client. A dictionary of
scope ids (OAuth2 scope identifiers), where the value for each id is either:

- '*' if the scope is applicable across all relevant platform entities; or
- a set of collection ids to which the scope's usage is limited (implemented
  as a list for JSON serialization)
"""


@dataclass
class UserInfo:
    sub: str
    email: str
    email_verified: bool
    name: Optional[str]
    picture: Optional[str]
    roles: list[str]


class AccessTokenModel(BaseModel):
    client_id: str
    user_id: Optional[str]
    permissions: Permissions


class ScopeModel(BaseModel):
    id: str
    type: str
