from typing import Optional

from pydantic import AnyHttpUrl, BaseModel, Field, validator

from odp.const import ID_REGEX
from odp.const.hydra import GrantType, ResponseType, TokenEndpointAuthMethod


class ClientModel(BaseModel):
    id: str
    name: str
    scope_ids: list[str]
    collection_specific: bool
    collection_keys: dict[str, str]
    grant_types: list[GrantType]
    response_types: list[ResponseType]
    redirect_uris: list[AnyHttpUrl]
    post_logout_redirect_uris: list[AnyHttpUrl]
    token_endpoint_auth_method: TokenEndpointAuthMethod
    allowed_cors_origins: list[AnyHttpUrl]
    client_credentials_grant_access_token_lifespan: Optional[str]


class ClientModelIn(BaseModel):
    id: str = Field(..., regex=ID_REGEX)
    name: str
    secret: str = Field(None, min_length=16)
    scope_ids: list[str]
    collection_specific: bool
    collection_ids: list[str]
    grant_types: list[GrantType]
    response_types: list[ResponseType]
    redirect_uris: list[AnyHttpUrl]
    post_logout_redirect_uris: list[AnyHttpUrl]
    token_endpoint_auth_method: TokenEndpointAuthMethod
    allowed_cors_origins: list[AnyHttpUrl]
    client_credentials_grant_access_token_lifespan: Optional[str] = Field(None, regex='^([0-9]+(ns|us|ms|s|m|h))*$')

    @validator('collection_ids')
    def validate_collection_ids(cls, collection_ids, values):
        try:
            if not values['collection_specific'] and collection_ids:
                raise ValueError("Collections can only be associated with a collection-specific client.")
        except KeyError:
            pass  # ignore: collection_specific validation already failed

        return collection_ids
