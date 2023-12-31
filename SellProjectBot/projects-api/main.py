from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger

from admin.admin import admin_router
from database import init_models


def create_logger() -> None:
    logger.add(
        "logs/debug.log",
        format="{time} {level} {message}",
        level="INFO",
        rotation="5 MB",
        compression="zip",
    )
    logger.info("Start app")


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_logger()
    await init_models()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(admin_router, prefix="/admin")

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    try:
        uvicorn.run("main:app", host="0.0.0.0", port=9999, reload=True)
    except (KeyboardInterrupt, SystemExit):
        logger.info("Stop app")
