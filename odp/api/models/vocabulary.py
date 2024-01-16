from typing import Any

from pydantic import BaseModel, Field

from odp.const import ID_REGEX


class VocabularyTermModel(BaseModel):
    id: str
    data: dict[str, Any]


class VocabularyTermModelIn(BaseModel):
    id: str = Field(..., regex=ID_REGEX)
    data: dict[str, Any]


class VocabularyModel(BaseModel):
    id: str
    scope_id: str
    schema_id: str
    schema_uri: str
    schema_: dict[str, Any]
    static: bool
    terms: list[VocabularyTermModel]
