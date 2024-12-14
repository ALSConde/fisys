from .ICreateIncomeRepo import ICreateIncomeRepo
from .IDeleteIncomeRepo import IDeleteIncomeRepo
from .ILoadIncomeRepo import ILoadIncomeRepo
from .IUpdateIncomeRepo import IUpdateIncomeRepo


class IIncomeRepo(
    ICreateIncomeRepo, IDeleteIncomeRepo, ILoadIncomeRepo, IUpdateIncomeRepo
): ...
