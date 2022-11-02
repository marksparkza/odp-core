from pydantic import AnyHttpUrl

from odp.config import BaseConfig
from odp.config.mixins import OAuth2ClientConfigMixin


class GoogleConfig(BaseConfig, OAuth2ClientConfigMixin):
    class Config:
        env_prefix = 'GOOGLE_'

    OPENID_URI: AnyHttpUrl  # Google OpenID configuration

    # enable/disable login via Google:
    # Google only allows redirects to public URLs or to localhost,
    # so it should be disabled, for example, on the dev platform
    ENABLE: bool
