from abc import ABC, abstractmethod

from models.wallets.Categories import Categories


class IUpdateCategoryRepo(ABC):
    @abstractmethod
    def update(self, category_id: int, category: Categories) -> Categories: ...
