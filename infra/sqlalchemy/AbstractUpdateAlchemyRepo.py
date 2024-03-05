from typing import Generic
from infra.sqlalchemy.AbstractAlchemyRepo import AbstractAlchemyRepo, M


class AbstractUpdateAlchemyRepo(AbstractAlchemyRepo[M]):
    async def update(self, id: int, model: M) -> M:
        self.session.merge(model)
        self.session.commit()
        self.session.refresh(model)
        return model
