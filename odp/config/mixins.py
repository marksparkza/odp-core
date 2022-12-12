from typing import List

from pydantic import BaseSettings


class DBConfigMixin(BaseSettings):
    HOST: str
    PORT: int = 5432
    NAME: str
    USER: str
    PASS: str
    ECHO: bool = False  # when True, SQLAlchemy emits SQL commands to stderr

    @property
    def URL(self) -> str:
        return f'postgresql://{self.USER}:{self.PASS}@{self.HOST}:{self.PORT}/{self.NAME}'


class OAuth2ClientConfigMixin(BaseSettings):
    CLIENT_ID: str
    CLIENT_SECRET: str
    SCOPE: List[str] = []


class ODPUIClientMixin(BaseSettings):
    """Config mixin for ODP Flask apps."""

    # user interface (authorization code grant)
    UI_CLIENT_ID: str
    UI_CLIENT_SECRET: str
    UI_CLIENT_SCOPE: List[str] = []

    # client interface (client credentials grant)
    CI_CLIENT_ID: str
    CI_CLIENT_SECRET: str
    CI_CLIENT_SCOPE: List[str] = []

    FLASK_SECRET: str
