from pydantic import BaseModel

from odp.const.db import ArchiveAdapter


class ArchiveModel(BaseModel):
    id: str
    url: str
    adapter: ArchiveAdapter
    scope_id: str
    resource_count: int
