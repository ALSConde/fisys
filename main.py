from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.responses import JSONResponse
from exceptions.APIError import APIError
from models.BaseModel import init
from configs.Environment import get_env
from configs.Log import logger
from routes.v1 import V1Router
from models.wallets.stocks.StockBuyHistory import StockBuyHistory
from models.wallets.stocks.StockSellHistory import StockSellHistory
from models.wallets.stocks.Stock import Stock
from models.wallets.Income import Income
from models.wallets.Expense import Expense
from models.wallets.Wallet import Wallet
from models.wallets.Categories import Categories

# Get environment variables
env = get_env()


# Create a context manager to start and stop the application
@asynccontextmanager
async def start_app(app: FastAPI):
    logger.info("Starting application")
    yield


# Create APP instance
app = FastAPI(title=env.APP_NAME, version=env.API_VERSION, lifespan=start_app)

# Include routes
app.include_router(V1Router)


@app.exception_handler(APIError)
async def api_error_handler(request, exc: APIError):
    match exc.status_code:
        case 500:
            logger.error(exc.message)
            return JSONResponse(
                status_code=exc.status_code,
                content={"message": "Internal Server Error"},
            )
        case _:
            logger.info(exc.message)
            return JSONResponse(
                status_code=exc.status_code,
                content={"message": exc.message},
            )


# Initialize Data Model Attributes
init()
