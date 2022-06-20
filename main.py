import uuid

from fastapi import FastAPI

import database
from repositories.user_repository import UserRepository

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

#userrp = UserRepository()

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
