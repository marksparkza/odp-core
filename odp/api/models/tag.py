from typing import Any, Optional

from pydantic import BaseModel

from odp.const.db import TagCardinality


class TagModel(BaseModel):
    id: str
    cardinality: TagCardinality
    public: bool
    scope_id: str
    schema_id: str
    schema_uri: str
    schema_: dict[str, Any]
    vocabulary_id: Optional[str]


class TagInstanceModel(BaseModel):
    id: str
    tag_id: str
    user_id: Optional[str]
    user_name: Optional[str]
    user_email: Optional[str]
    data: dict[str, Any]
    timestamp: str
    cardinality: TagCardinality
    public: bool
    vocabulary_id: Optional[str]
    keyword_id: Optional[int]
    keyword: Optional[str]


class TagInstanceModelIn(BaseModel):
    tag_id: str
    data: dict[str, Any]
    keyword_id: Optional[int]
