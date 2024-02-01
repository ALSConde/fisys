from abc import ABC, abstractmethod
from models import User


class ILoadUserRepo(ABC):
    @abstractmethod
    async def load_by(self, **kwargs) -> User | None: ...
