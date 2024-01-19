from typing import Any, Optional

from pydantic import AnyHttpUrl, BaseModel, Field


class CatalogModel(BaseModel):
    id: str
    url: str
    record_count: int


class CatalogModelWithData(CatalogModel):
    data: Optional[dict[str, Any]]
    timestamp: Optional[str]


class PublishedMetadataModel(BaseModel):
    schema_id: str
    schema_uri: str
    metadata: dict[str, Any]


class PublishedTagInstanceModel(BaseModel):
    tag_id: str
    data: dict[str, Any]
    user_name: Optional[str]
    timestamp: str


class PublishedRecordModel(BaseModel):
    pass


class PublishedSAEONRecordModel(PublishedRecordModel):
    id: str
    doi: Optional[str]
    sid: Optional[str]
    collection_key: str
    collection_name: str
    provider_key: str
    provider_name: str
    metadata_records: list[PublishedMetadataModel]
    tags: list[PublishedTagInstanceModel]
    keywords: Optional[list[str]]
    spatial_north: Optional[float]
    spatial_east: Optional[float]
    spatial_south: Optional[float]
    spatial_west: Optional[float]
    temporal_start: Optional[str]
    temporal_end: Optional[str]
    timestamp: str
    published: bool = Field(True, const=True)
    searchable: Optional[bool]


class PublishedDataCiteRecordModel(PublishedRecordModel):
    doi: str
    url: Optional[AnyHttpUrl]
    metadata: dict[str, Any]


class RetractedRecordModel(BaseModel):
    id: str
    published: bool = Field(False, const=False)


class SearchResult(BaseModel):
    facets: dict[str, list[tuple[str, int]]]  # facet: [(value, count)]
    items: list[PublishedSAEONRecordModel]
    total: int
    page: int
    pages: int


class CatalogRecordModel(BaseModel):
    catalog_id: str
    record_id: str
    published: bool
    published_record: Optional[PublishedSAEONRecordModel | PublishedDataCiteRecordModel]
    reason: str
    timestamp: str
    external_synced: Optional[bool]
    external_error: Optional[str]
    external_error_count: Optional[int]
    index_full_text: Optional[str]
    index_keywords: Optional[list[str]]
    index_facets: Optional[list[dict[str, str]]]
    index_spatial_north: Optional[float]
    index_spatial_east: Optional[float]
    index_spatial_south: Optional[float]
    index_spatial_west: Optional[float]
    index_temporal_start: Optional[str]
    index_temporal_end: Optional[str]
    index_searchable: Optional[bool]
