from .AbstractAlchemyRepo import AbstractAlchemyRepo, M


class AbstractDeleteAlchemyRepo(AbstractAlchemyRepo[M]):
    async def delete(self, id: int) -> None:
        self.session.query(self.model).filter(self.model.id == id).delete()
        self.session.commit()
        self.session.flush()
