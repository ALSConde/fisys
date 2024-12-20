from fastapi import APIRouter
from .AuthRouter import AuthRouter
from .userRoutes import CreateRouter as UserCreateRouter, LoadRouter, DeleteRouter, UpdateRouter
from .walletRoutes import CreateRouter as WalletCreateRouter

# V1 User Routes
V1Router = APIRouter(prefix="/v1", tags=["v1"])
V1Router.include_router(UserCreateRouter)
V1Router.include_router(LoadRouter)
V1Router.include_router(UpdateRouter)
V1Router.include_router(DeleteRouter)
V1Router.include_router(WalletCreateRouter)

# V1 Auth Routes
V1Router.include_router(AuthRouter)


__all__ = ["V1Router"]
