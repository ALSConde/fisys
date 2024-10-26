from typing import Generic, Type
from .AbstractAlchemyRepo import AbstractAlchemyRepo, M


class AbstractLoadAlchemyRepo(AbstractAlchemyRepo[M]):

    async def load_by(self, **kwargs) -> list[M] | M | None:
        query = self.session.query(self.model)
        for field, value in kwargs.items():
            query = query.filter(getattr(self.model, field).like(f"%{value}%"))
        return query.all()

    async def load_first(self, **kwargs) -> M | None:
        query = self.session.query(self.model)
        for field, value in kwargs.items():
            query = query.filter(getattr(self.model, field).like(f"%{value}%"))
        return query.first()
