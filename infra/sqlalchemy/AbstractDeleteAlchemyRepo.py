from .AbstractAlchemyRepo import AbstractAlchemyRepo, M

class AbstractDeleteAlchemyRepo(AbstractAlchemyRepo[M]):
    async def delete(self, id: int) -> None:
        model = self.session.query(self.model).filter_by(id=id, active=True)
        model.update({"active": False})
        self.session.commit()
        self.session.flush()
        