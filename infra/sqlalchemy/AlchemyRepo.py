from infra.sqlalchemy.AbstractAlchemyRepo import M
from infra.sqlalchemy.AbstractLoadByAlchemyRepo import AbstractLoadByAlchemyRepo
from infra.sqlalchemy.AbstractCreateAlchemyRepo import AbstractCreateAlchemyRepo
from infra.sqlalchemy.AbstractUpdateAlchemyRepo import AbstractUpdateAlchemyRepo



class AlchemyRepo(AbstractCreateAlchemyRepo[M], AbstractLoadByAlchemyRepo[M], AbstractUpdateAlchemyRepo[M]):
    def __init__(self) -> None:
        super().__init__()
        