from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from database import Base
from models.base_model import BaseModel
from models.item import Item


class User(BaseModel, Base):
    __tablename__ = "users"

    email = Column(String, unique=True, index=True)
    password = Column(String)

    items = relationship("Item", back_populates="owner")

