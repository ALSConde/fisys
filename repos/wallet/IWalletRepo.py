from .ILoadWalletRepo import ILoadWalletRepo
from .ICreateWalletRepo import ICreateWalletRepo
from .IDeleteWalletRepo import IDeleteWalletRepo
from .IUpdateWalletRepo import IUpdateWalletRepo


class IWalletRepo(
    ICreateWalletRepo, IDeleteWalletRepo, IUpdateWalletRepo, ILoadWalletRepo
): ...
