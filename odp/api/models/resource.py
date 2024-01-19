from typing import Optional

from pydantic import BaseModel, validator


class ResourceModel(BaseModel):
    id: str
    provider_id: str
    provider_key: str
    archive_id: str
    path: str
    type: ResourceType
    name: Optional[str]
    size: Optional[int]
    md5: Optional[str]
    timestamp: str


class ResourceModelIn(BaseModel):
    provider_id: str
    archive_id: str
    path: str
    type: ResourceType
    name: Optional[str]
    size: Optional[int]
    md5: Optional[str]
    timestamp: Optional[str]
    text_data: Optional[str]
    binary_data: Optional[bytes]

    @validator('path')
    def validate_path(cls, path: str):
        if not path.startswith('/'):
            raise ValueError("path must start with '/'")

        return path
