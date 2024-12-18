from abc import ABC, abstractmethod


class IDeleteCategoryRepo(ABC):
    @abstractmethod
    def delete(self, category_id: int) -> None: ...
