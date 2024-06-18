from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field

from odp.const.db import KeywordStatus


class KeywordModel(BaseModel):
    key: str
    data: dict
    status: KeywordStatus
    schema_id: Optional[str] = Field(None, title="The keyword's validating schema")
    keywords: Optional[list[KeywordModel]]


class KeywordModelIn(BaseModel):
    data: dict


class KeywordModelAdmin(KeywordModelIn):
    status: KeywordStatus
    schema_id: Optional[str] = Field(None, title="The validating schema for sub-keywords "
                                                 "(inherited from the parent by default)")
