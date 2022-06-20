import string
import uuid

from sqlalchemy.orm import Session

from models.abstract.user_abc import UserAbc
from models.user import User


class UserRepository(UserAbc):
    def get_user_by_email(self, db: Session, email: string):
        return db.query(User).filter(User.email == email).first()

    def create(self, db: Session, user: User): #should be use pydantic schemas
        db_user = User(email=user.email, password=user.password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    def update(self, db: Session, user: User):
        pass

    def get(self, db: Session, uuid: uuid):
        pass

    def delete(self, db: Session, uuid: uuid):
        pass
