from typing import Any, Optional

from odp.api.models.resource import ResourceModel, ResourceModelIn
from pydantic import BaseModel


class PackageModel(BaseModel):
    id: str
    provider_id: str
    provider_key: str
    record_id: Optional[str]
    metadata: Optional[dict[str, Any]]
    timestamp: str
    resources: list[ResourceModel]


class PackageModelIn(BaseModel):
    provider_id: str
    metadata: Optional[dict[str, Any]]
    resource_ids: list[str]  # existing
    resources: list[ResourceModelIn]  # new
