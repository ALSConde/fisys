from typing import TypeVar, Generic

from fastapi import Depends
from configs.Database import get_db
from models import BaseModel
from sqlalchemy.orm import Session

M = TypeVar("M", bound=BaseModel)


class AbstractAlchemyRepo(Generic[M]):
    session: Session

    def __init__(self, session: Session = Depends(get_db)):
        self.session = session
