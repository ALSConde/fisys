from typing import TypeVar, Generic
from fastapi import Depends
from configs.Database import get_db
from models.BaseModel import BaseModel
from sqlalchemy.orm import Session

M = TypeVar("M", bound=BaseModel)


class AbstractAlchemyRepo(Generic[M]):
    session: Session
    model: M

    def __init__(self, model: BaseModel, session: Session = Depends(get_db)):
        self.session = session
        self.model = model
