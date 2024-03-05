from fastapi import APIRouter
from .AuthRouter import AuthRouter
from .userRoutes import CreateRouter

V1Router = APIRouter(prefix="/v1", tags=["v1"])
V1Router.include_router(AuthRouter)
V1Router.include_router(CreateRouter)

__all__ = ["V1Router"]
