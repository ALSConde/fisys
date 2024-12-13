from .AbstractAlchemyRepo import M, AbstractAlchemyRepo


class AbstractUpdateAlchemyRepo(AbstractAlchemyRepo[M]):
    async def update(self, id: int, model: M) -> M:
        self.session.query(self.model).filter_by(id=id, active=True).update(model.normalize())
        self.session.commit()
        self.session.flush()
        return model
