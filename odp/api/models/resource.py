from typing import Optional

from pydantic import BaseModel, Field

from odp.const.db import HashAlgorithm


class ResourceModel(BaseModel):
    id: str
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
    archive_paths: dict[str, str] = Field(..., title='Mapping of archive id to resource path (relative to archive url)')
    package_paths: dict[str, str] = Field(..., title='Mapping of package id to resource path (relative to package root)')
