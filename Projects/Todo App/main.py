from contextlib import asynccontextmanager

from fastapi import FastAPI

from database import create_all_tables
from router import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_all_tables()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(router)
