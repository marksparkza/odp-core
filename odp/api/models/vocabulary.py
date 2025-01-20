from typing import Any

from pydantic import BaseModel


class VocabularyModel(BaseModel):
    id: str
    uri: str
    schema_id: str
    schema_uri: str
    schema_: dict[str, Any]
    static: bool
    keyword_count: int
