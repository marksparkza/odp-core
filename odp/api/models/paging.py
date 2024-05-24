from typing import Generic, List, TypeVar

from pydantic import BaseModel
from pydantic.generics import GenericModel

GenericAPIModel = TypeVar('GenericAPIModel', bound=BaseModel)


class Page(GenericModel, Generic[GenericAPIModel]):
    items: List[GenericAPIModel]
    total: int
    page: int
    pages: int
