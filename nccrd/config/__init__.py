from pydantic.networks import AnyHttpUrl

from odp.config.base import BaseConfig
from odp.config.mixins import AppConfigMixin, DBConfigMixin


class NCCRDDBConfig(BaseConfig, DBConfigMixin):
    class Config:
        env_prefix = 'NCCRD_DB_'


class NCCRDWebConfig(BaseConfig, AppConfigMixin):
    class Config:
        env_prefix = 'NCCRD_WEB_'


class NCCRDConfig(BaseConfig):
    class Config:
        env_prefix = 'NCCRD_'

    API_URL: AnyHttpUrl = None

    _subconfig = {
        'DB': NCCRDDBConfig,
        'WEB': NCCRDWebConfig
    }


class Config(BaseConfig):
    _subconfig = {
        'NCCRD': NCCRDConfig,
    }


nccrd_config = Config()
