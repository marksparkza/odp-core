from pydantic import BaseModel, Field

from odp.const import ID_REGEX


class ProviderModel(BaseModel):
    id: str
    key: str
    name: str
    collection_keys: dict[str, str]
    timestamp: str


class ProviderModelIn(BaseModel):
    key: str = Field(..., regex=ID_REGEX)
    name: str
