from .IDeleteExpanseRepo import IDeleteExpanseRepo
from .ILoadExpanseRepo import ILoadExpanseRepo
from .IUpdateExpanseRepo import IUpadteExpanseRepo
from .ICreateExpanseRepo import ICreateExpanseRepo


class IExpanseRepo(
    ICreateExpanseRepo, IDeleteExpanseRepo, ILoadExpanseRepo, IUpadteExpanseRepo
): ...
