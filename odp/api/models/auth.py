from dataclasses import dataclass
from typing import Literal, Optional

from pydantic import BaseModel

Permission = Literal['*'] | list[str]
"""Represents a granted scope along with its applicability.

- '*' if the scope is applicable to all relevant entities
- list of object ids to which the scope's usage is restricted
"""

Permissions = dict[str, Permission]
"""The effective set of permissions for a user or a client. A dictionary of
scope ids (OAuth2 scope identifiers), where the value for each id indicates
the applicability of the scope.
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
