from abc import ABC
from .ICreateUserRepo import ICreateUserRepo
from .IUpdateUserRepo import IUpdateUserRepo
from .ILoadUserRepo import ILoadUserRepo


class IUserRepo(ILoadUserRepo, ICreateUserRepo, IUpdateUserRepo, ABC):
    ...
