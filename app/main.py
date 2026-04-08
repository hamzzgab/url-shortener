from fastapi import FastAPI

from app.database import lifespan
from app.routers import urls

app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return {"message": "Welcome to Url Shortener"}


app.include_router(urls.router)
