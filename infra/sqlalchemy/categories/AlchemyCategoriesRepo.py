from infra.sqlalchemy.AlchemyRepo import AlchemyRepo
from models.wallets.Categories import Categories
from repos.category.ICategoryRepo import ICategoryRepo
from sqlalchemy.orm import Session
from fastapi import Depends
from configs.Database import get_db


class AlchemyCategoriesRepo(AlchemyRepo[Categories], ICategoryRepo):
    def __init__(self, session: Session = Depends(get_db)) -> None:
        super().__init__(Categories, session)
