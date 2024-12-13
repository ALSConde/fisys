from .ICreateStockRepo import ICreateStockRepo
from .ILoadStockRepo import ILoadStockRepo
from .IUpdateStockRepo import IUpdateStockRepo


class IStockRepo(ICreateStockRepo, ILoadStockRepo, IUpdateStockRepo): ...
