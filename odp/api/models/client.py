from typing import Optional

from pydantic import AnyHttpUrl, BaseModel, Field, validator

from odp.const import ID_REGEX
from odp.const.hydra import GrantType, ResponseType, TokenEndpointAuthMethod


class ClientModel(BaseModel):
    id: str
    name: str
    scope_ids: list[str]
    provider_specific: bool
    provider_id: Optional[str]
    provider_key: Optional[str]
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
    provider_specific: bool
    provider_id: Optional[str]
    grant_types: list[GrantType]
    response_types: list[ResponseType]
    redirect_uris: list[AnyHttpUrl]
    post_logout_redirect_uris: list[AnyHttpUrl]
    token_endpoint_auth_method: TokenEndpointAuthMethod
    allowed_cors_origins: list[AnyHttpUrl]
    client_credentials_grant_access_token_lifespan: Optional[str] = Field(None, regex='^([0-9]+(ns|us|ms|s|m|h))*$')

    @validator('provider_id')
    def validate_provider_id(cls, provider_id, values):
        try:
            provider_specific = values['provider_specific']

            if provider_specific and not provider_id:
                raise ValueError('A provider must be associated with a provider-specific client.')

            if provider_id and not provider_specific:
                raise ValueError('A provider may only be associated with a provider-specific client.')

        except KeyError:
            pass  # ignore: provider_specific validation already failed

        return provider_id
