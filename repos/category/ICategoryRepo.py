from repos.category.IUpdateCategoryRepo import IUpdateCategoryRepo
from .IDeleteCategoryRepo import IDeleteCategoryRepo
from .ILoadCategoryRepo import ILoadCategoryRepo
from .ICreateCategoryRepo import ICreateCategoryRepo


class ICategoryRepo(
    ICreateCategoryRepo, ILoadCategoryRepo, IDeleteCategoryRepo, IUpdateCategoryRepo
): ...
