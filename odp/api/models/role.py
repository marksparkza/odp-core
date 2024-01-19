from pydantic import BaseModel, Field, validator

from odp.const import ID_REGEX


class RoleModel(BaseModel):
    id: str
    scope_ids: list[str]
    collection_specific: bool
    collection_keys: dict[str, str]


class RoleModelIn(BaseModel):
    id: str = Field(..., regex=ID_REGEX)
    scope_ids: list[str]
    collection_specific: bool
    collection_ids: list[str]

    @validator('collection_ids')
    def validate_collection_ids(cls, collection_ids, values):
        try:
            if not values['collection_specific'] and collection_ids:
                raise ValueError("Collections can only be associated with a collection-specific role.")
        except KeyError:
            pass  # ignore: collection_specific validation already failed

        return collection_ids
