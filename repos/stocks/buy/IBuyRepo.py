from .ICreateBuyRepo import ICreateBuyRepo
from .IDeleteBuyRepo import IDeleteBuyRepo
from .ILoadBuyRepo import ILoadBuyRepo
from .IUpdateBuyRepo import IUpdateBuyRepo


class IBuyRepo(ICreateBuyRepo, IDeleteBuyRepo, IUpdateBuyRepo, ILoadBuyRepo): ...
