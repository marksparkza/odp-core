from typing import Optional

from pydantic import BaseModel, Field


class ResourceModel(BaseModel):
    id: str
    title: str
    description: Optional[str]
    filename: Optional[str]
    mimetype: Optional[str]
    size: Optional[int]
    md5: Optional[str]
    timestamp: str
    provider_id: str
    provider_key: str
    archive_urls: dict[str, str] = Field(..., title='Mapping of archive IDs to resource URLs')


class ResourceModelIn(BaseModel):
    title: str
    description: Optional[str]
    filename: Optional[str]
    mimetype: Optional[str]
    size: Optional[int]
    md5: Optional[str]
    provider_id: str
    archive_id: str
    archive_path: str = Field(..., regex=r'^\S*$', title='Resource path relative to archive URL')
