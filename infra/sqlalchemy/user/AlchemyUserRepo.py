from infra.sqlalchemy.AlchemyRepo import AlchemyRepo
from models import User
from repos.user import IUserRepo


class AlchemyUserRepo(IUserRepo, AlchemyRepo[User]):
    def __init__(self) -> None:
        super().__init__()

    async def create(self, user: User) -> User:
        return await super().create(user)
    
    async def load_by(self, **kwargs) -> User:
        return await super().load_by(**kwargs)
    
    async def update(self, user_id : int, user: User) -> User:
        return await super().update(user_id, user)
    