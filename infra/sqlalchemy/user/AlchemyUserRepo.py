from infra.sqlalchemy.AbstractCreateAlchemyRepo import AbstractCreateAlchemyRepo
from infra.sqlalchemy.AbstractLoadByAlchemyRepo import AbstractLoadByAlchemyRepo
from models import User
from repos.user import IUserRepo


class AlchemyUserRepo(IUserRepo, AbstractCreateAlchemyRepo[User], AbstractLoadByAlchemyRepo[User]):
    def __init__(self) -> None:
        super().__init__()