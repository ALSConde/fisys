from .IDeleteSellRepo import IDeleteSellRepo
from .ICreateSellRepo import ICreateSellRepo
from .IUpdateSellRepo import IUpdateSellRepo
from .ILoadSellRepo import ILoadSellRepo


class ISellRepo(ICreateSellRepo, IUpdateSellRepo, IDeleteSellRepo, ILoadSellRepo): ...
