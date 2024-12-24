from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field, root_validator

from odp.const.db import KeywordStatus


class KeywordModel(BaseModel):
    vocabulary_id: str
    id: int
    key: str
    data: dict
    status: KeywordStatus
    parent_id: Optional[int] = Field(None, title='Parent keyword id')
    parent_key: Optional[str] = Field(None, title='Parent keyword')


class KeywordAncestorModel(BaseModel):
    vocabulary_id: str
    id: int
    key: str
    data: dict
    status: KeywordStatus
    ids: list[int] = Field(..., title='Keyword id hierarchy, from root to self')
    keys_: list[str] = Field(..., title='Keyword key hierarchy, from root to self')


class KeywordHierarchyModel(KeywordModel):
    child_keywords: list[KeywordHierarchyModel]


class KeywordModelIn(BaseModel):
    key: str = Field(..., title='The keyword; copied to data["key"]')
    data: dict = Field(..., title='Keyword data; validated against vocabulary schema')
    parent_id: Optional[int] = Field(None, title='Parent keyword id')

    @root_validator
    def set_data_key(cls, values):
        """Copy `key` into `data` post-validation."""
        try:
            values['data']['key'] = values['key']
        except KeyError:
            pass  # ignore - field validation already failed

        return values


class KeywordModelAdmin(KeywordModelIn):
    status: KeywordStatus
