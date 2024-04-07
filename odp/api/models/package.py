from typing import Any, Optional

from pydantic import BaseModel, validator

from odp.const import ODPMetadataSchema


class PackageModel(BaseModel):
    id: str
    provider_id: str
    provider_key: str
    schema_id: str
    metadata: dict[str, Any]
    validity: dict[str, Any]
    notes: Optional[str]
    timestamp: str
    resource_count: int
    record_id: Optional[str]
    record_doi: Optional[str]
    record_sid: Optional[str]


class PackageModelIn(BaseModel):
    provider_id: str
    schema_id: str
    metadata: dict[str, Any]
    notes: Optional[str]
    resource_ids: list[str]

    @validator('schema_id')
    def validate_schema_id(cls, schema_id):
        if schema_id not in (ODPMetadataSchema.SAEON_DATACITE4, ODPMetadataSchema.SAEON_ISO19115):
            raise ValueError("SAEON metadata schema required")

        return schema_id
