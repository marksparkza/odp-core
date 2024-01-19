from typing import Any

from pydantic import BaseModel


class SchemaModel(BaseModel):
    id: str
    type: str
    uri: str
    schema_: dict[str, Any]
