from abc import ABC, abstractmethod
from models import User


class ILoadUserRepo(ABC):
    @abstractmethod
    async def load_actives_by(self, **kwargs) -> list[User] | None: ...

    @abstractmethod
    async def load_active_first(self, **kwargs) -> User | None: ...

    @abstractmethod
    async def load_all(self) -> list[User]: ...

    @abstractmethod
    async def load_all_actives(self) -> list[User]: ...

    @abstractmethod
    async def load_all_inactives(self) -> list[User]: ...

    @abstractmethod
    async def load_by(self, **kwargs) -> User | list[User] | None: ...