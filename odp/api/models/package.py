from typing import Optional

from pydantic import BaseModel, validator

from odp.api.models.resource import ResourceModel
from odp.api.models.tag import TagInstanceModel
from odp.const import ODPMetadataSchema
from odp.const.db import PackageStatus


class PackageModel(BaseModel):
    id: str
    key: str
    status: PackageStatus
    timestamp: str
    provider_id: str
    provider_key: str
    resource_ids: list[str]
    schema_id: str
    schema_uri: str
    record_id: Optional[str]
    record_doi: Optional[str]
    record_sid: Optional[str]


class PackageDetailModel(PackageModel):
    resources: list[ResourceModel]
    tags: list[TagInstanceModel]
    metadata: Optional[dict]
    validity: Optional[dict]


class PackageModelIn(BaseModel):
    provider_id: str
    schema_id: str

    @validator('schema_id')
    def validate_schema_id(cls, schema_id):
        if schema_id not in (ODPMetadataSchema.SAEON_DATACITE4, ODPMetadataSchema.SAEON_ISO19115):
            raise ValueError("SAEON metadata schema required")

        return schema_id
