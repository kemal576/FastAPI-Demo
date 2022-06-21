import string
import uuid

from sqlalchemy.orm import Session

from models.user import User
from schemas.user import UserCreate


class UserRepository:
    @classmethod
    def get_user_by_email(cls, db: Session, email: string):
        return db.query(User).filter(User.email == email)

    @classmethod
    def create(cls, db: Session, user: UserCreate):  # should be use pydantic schemas
        db_user = User(email=user.email, password=user.password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    @classmethod
    def update(cls, db: Session, user: User):
        pass

    @classmethod
    def get(cls, db: Session, user_id: uuid):
        return db.query(User).filter(User.id == user_id)

    @classmethod
    def delete(cls, db: Session, user_id: uuid):
        user = db.query(User).get(user_id)
        if user:
            db.delete(user)
