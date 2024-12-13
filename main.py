from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.responses import JSONResponse
from exceptions.APIError import APIError
from models.BaseModel import init
from configs.Environment import get_env
from routes.v1 import V1Router
from models.wallets.stocks.StockBuyHistory import StockBuyHistory
from models.wallets.stocks.StockSellHistory import StockSellHistory

# Get environment variables
env = get_env()


# Create a context manager to start and stop the application
@asynccontextmanager
async def start_app(app: FastAPI):
    yield


# Create APP instance
app = FastAPI(title=env.APP_NAME, version=env.API_VERSION, lifespan=start_app)

# Include routes
app.include_router(V1Router)


@app.exception_handler(APIError)
async def api_error_handler(request, exc: APIError):
    return JSONResponse(
        status_code=exc.code,
        content={"detail": exc.message},
    )


# Initialize Data Model Attributes
init()
