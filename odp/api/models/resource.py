from typing import Optional

from pydantic import BaseModel, Field

from odp.const.db import HashAlgorithm


class ResourceModel(BaseModel):
    id: str
    title: Optional[str]
    description: Optional[str]
    folder: str
    filename: str
    mimetype: Optional[str]
    size: Optional[int]
    hash: Optional[str]
    hash_algorithm: Optional[HashAlgorithm]
    timestamp: str
    package_id: str
    package_key: str
    package_path: str
    archive_paths: dict[str, str] = Field(..., title='Mapping of archive id to resource path relative to archive url(s)')
