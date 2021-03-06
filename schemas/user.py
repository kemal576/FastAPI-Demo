from pydantic import BaseModel

from schemas.item import Item


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    items: list[Item] = []

    class Config:
        orm_mode = True
        # arbitrary_types_allowed = True
