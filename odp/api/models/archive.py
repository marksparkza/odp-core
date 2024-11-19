from typing import Optional

from pydantic import BaseModel

from odp.const.db import ArchiveAdapter


class ArchiveModel(BaseModel):
    id: str
    download_url: Optional[str]
    upload_url: Optional[str]
    adapter: ArchiveAdapter
    scope_id: str
    resource_count: int
