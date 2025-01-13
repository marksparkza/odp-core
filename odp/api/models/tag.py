from typing import Any, Optional

from pydantic import BaseModel, Field

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
    keyword_ids: Optional[list[int]] = Field(None, title='Keyword id hierarchy, from root to selected')
    keyword_keys: Optional[list[str]] = Field(None, title='Keyword key hierarchy, from root to selected')


class TagInstanceModelIn(BaseModel):
    tag_id: str
    data: dict[str, Any]
    keyword: Optional[str]
