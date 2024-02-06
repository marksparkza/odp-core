from pydantic import BaseModel


class ArchiveModel(BaseModel):
    id: str
    url: str
    resource_count: int
