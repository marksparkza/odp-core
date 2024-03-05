from typing import Optional

from pydantic import BaseModel, Field

from odp.api.models.tag import TagInstanceModel
from odp.const import ID_REGEX


class CollectionModel(BaseModel):
    id: str
    key: str
    name: str
    doi_key: Optional[str]
    provider_id: str
    provider_key: str
    record_count: int
    tags: list[TagInstanceModel]
    role_ids: list[str]
    timestamp: str


class CollectionModelIn(BaseModel):
    key: str = Field(..., regex=ID_REGEX)
    name: str
    doi_key: Optional[str]
    provider_id: str
