from pydantic.networks import AnyHttpUrl

from odp.config.base import BaseConfig
from odp.config.mixins import AppConfigMixin, DBConfigMixin


class SOMISANADBConfig(BaseConfig, DBConfigMixin):
    class Config:
        env_prefix = 'SOMISANA_DB_'


class SOMISANAWebConfig(BaseConfig, AppConfigMixin):
    class Config:
        env_prefix = 'SOMISANA_WEB_'


class SOMISANAConfig(BaseConfig):
    class Config:
        env_prefix = 'SOMISANA_'

    API_URL: AnyHttpUrl = None

    _subconfig = {
        'DB': SOMISANADBConfig,
        'WEB': SOMISANAWebConfig
    }


class Config(BaseConfig):
    _subconfig = {
        'SOMISANA': SOMISANAConfig,
    }


somisana_config = Config()
