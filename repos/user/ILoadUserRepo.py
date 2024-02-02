from abc import ABC, abstractmethod
from models import User


class ILoadUserRepo(ABC):
    @abstractmethod
    async def load_by(self, **kwargs) -> User | None: ...

    @abstractmethod
    async def load_all(self, **kwargs) -> list[User] | None: ...
