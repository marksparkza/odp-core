from typing import Optional

from pydantic import BaseModel

from odp.const.db import ArchiveAdapter, HashAlgorithm


class ArchiveModel(BaseModel):
    id: str
    url: str
    adapter: ArchiveAdapter
    scope_id: str
    resource_count: int


class ArchiveResourceModel(BaseModel):
    archive_id: str
    resource_id: str
    path: str
    title: Optional[str]
    description: Optional[str]
    filename: Optional[str]
    mimetype: Optional[str]
    size: Optional[int]
    hash: Optional[str]
    hash_algorithm: Optional[HashAlgorithm]
    timestamp: str
    provider_id: str
    provider_key: str
