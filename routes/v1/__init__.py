from fastapi import APIRouter
from .AuthRouter import AuthRouter

V1Router = APIRouter(prefix="/v1", tags=["v1"])
V1Router.include_router(AuthRouter)

__all__ = ["V1Router"]
