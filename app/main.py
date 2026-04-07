from fastapi import FastAPI

from app.routers import urls

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to Url Shortener"}


app.include_router(urls.router)
