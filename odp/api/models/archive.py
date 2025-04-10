from typing import Optional

from pydantic import BaseModel


class ArchiveModel(BaseModel):
    id: str
    type: str
    scope_id: str
    upload_url: Optional[str]
    download_url: Optional[str]
    resource_count: int
