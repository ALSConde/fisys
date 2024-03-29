from typing import Generic
from .AbstractAlchemyRepo import AbstractAlchemyRepo, M


class AbstractLoadByAlchemyRepo(Generic[M], AbstractAlchemyRepo[M]):
    async def load_by(self, **kwargs) -> M.__class__ | None:
        ret = self.session.query(M.__class__).filter_by(**kwargs).first()
        return ret

    async def load_all(self, **kwargs) -> list[M.__class__] | None:
        ret = self.session.query(M.__class__).filter_by(**kwargs).all()
        return ret