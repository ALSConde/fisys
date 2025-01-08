from fastapi import APIRouter
from .AuthRouter import AuthRouter
from .userRoutes import (
    CreateRouter as UserCreateRouter,
    LoadRouter as UserLoadRouter,
    DeleteRouter,
    UpdateRouter,
)
from .walletRoutes import (
    CreateRouter as WalletCreateRouter,
    LoadRouter as WalletLoadRouter,
)

# V1 User Routes
V1Router = APIRouter(prefix="/v1", tags=["v1"])
V1Router.include_router(UserCreateRouter)
V1Router.include_router(UserLoadRouter)
V1Router.include_router(UpdateRouter)
V1Router.include_router(DeleteRouter)

# V1 Auth Routes
V1Router.include_router(AuthRouter)

# V1 Wallet Routes
V1Router.include_router(WalletCreateRouter)
V1Router.include_router(WalletLoadRouter)

# Export V1Router
__all__ = ["V1Router"]
