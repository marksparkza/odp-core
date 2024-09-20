from typing import Optional

from pydantic import BaseModel, Field, validator

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
    archive_paths: dict[str, str] = Field(..., title='Mapping of archive id to resource path')


class ResourceModelIn(BaseModel):
    title: Optional[str]
    description: Optional[str]
    filename: Optional[str]
    mimetype: Optional[str]
    size: Optional[int]
    hash_algorithm: Optional[HashAlgorithm]
    hash: Optional[str]
    provider_id: str
    archive_id: str
    archive_path: str = Field(..., regex=r'^\S*$', title='Resource path relative to archive URL')

    @validator('filename', always=True)
    def validate_filename(cls, filename, values):
        if not filename and not values.get('title'):
            raise ValueError('title and/or filename must be given')

        return filename

    @validator('hash')
    def validate_hash(cls, hash, values):
        try:
            if hash is not None and not values['hash_algorithm']:
                raise ValueError('hash_algorithm must be supplied with hash')
        except KeyError:
            pass  # ignore: hash_algorithm already failed validation

        return hash
