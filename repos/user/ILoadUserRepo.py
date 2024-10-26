from abc import ABC, abstractmethod
from models import User


class ILoadUserRepo(ABC):
    @abstractmethod
    async def load_by(self, **kwargs) -> list[User] | None: ...

    @abstractmethod
    async def load_first(self, **kwargs) -> User | None: ...
