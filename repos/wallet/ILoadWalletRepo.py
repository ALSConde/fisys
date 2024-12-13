from abc import ABC, abstractmethod


class ILoadWalletRepo(ABC):
    @abstractmethod
    async def load_by(self, **kwargs): ...

    @abstractmethod
    async def load_all(self): ...

    @abstractmethod
    async def load_first(self, **kwargs): ...
