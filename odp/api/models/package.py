from typing import Optional

from pydantic import BaseModel

from odp.api.models.resource import ResourceModel
from odp.const.db import PackageStatus


class PackageModel(BaseModel):
    id: str
    title: str
    status: PackageStatus
    notes: Optional[str]
    timestamp: str
    provider_id: str
    provider_key: str
    resource_ids: list[str]
    record_id: Optional[str]
    record_doi: Optional[str]
    record_sid: Optional[str]


class PackageDetailModel(PackageModel):
    resources: list[ResourceModel]


class PackageModelIn(BaseModel):
    title: str
    notes: Optional[str]
    provider_id: str
    resource_ids: list[str]
