from fastapi import FastAPI

import database
from routers import user

database.Base.metadata.create_all(bind=database.engine)

app = FastAPI()
app.include_router(user.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
