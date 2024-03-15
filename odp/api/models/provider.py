from pydantic import BaseModel, Field

from odp.const import ID_REGEX


class ProviderModel(BaseModel):
    id: str
    key: str
    name: str
    collection_keys: dict[str, str] = Field(..., title='Collection id:key pairs')
    user_names: dict[str, str] = Field(..., title='User id:name pairs')
    timestamp: str


class ProviderModelIn(BaseModel):
    key: str = Field(..., regex=ID_REGEX)
    name: str
    user_ids: list[str]
