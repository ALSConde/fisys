from fastapi import APIRouter
from .AuthRouter import AuthRouter
from .userRoutes import CreateRouter, LoadRouter, DeleteRouter, UpdateRouter

# V1 User Routes
V1Router = APIRouter(prefix="/v1", tags=["v1"])
V1Router.include_router(CreateRouter)
V1Router.include_router(LoadRouter)
V1Router.include_router(UpdateRouter)
V1Router.include_router(DeleteRouter)

# V1 Auth Routes
V1Router.include_router(AuthRouter)


__all__ = ["V1Router"]
