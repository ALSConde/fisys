from typing import TypeVar, Generic
from pydantic import BaseModel
from abc import ABC, abstractmethod

Request = TypeVar("Request", bound=BaseModel)
Response = TypeVar("Response", bound=BaseModel)


class IService(Generic[Request, Response], ABC):
    @abstractmethod
    def execute(self, dto: Request) -> Response:
        ...
