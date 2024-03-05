from typing import Generic, Type
from .AbstractAlchemyRepo import AbstractAlchemyRepo, M


class AbstractLoadAlchemyRepo(AbstractAlchemyRepo[M]):
    
    async def load_by(self, **kwargs) -> M | None:
        return self.session.query(self.model).filter_by(**kwargs).first()

    async def load_all(self, **kwargs) -> list[M] | M | None:
        return self.session.query(self.model).filter_by(**kwargs).all()
