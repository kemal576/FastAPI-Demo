import string
from abc import ABC, abstractmethod

from sqlalchemy.orm import Session

from models.abstract.repository import Repository
from models.user import User


class UserAbc(Repository, ABC):
    @abstractmethod
    def get_user_by_email(self, db: Session, email: string):
        pass

    @abstractmethod
    def create(self, db: Session, user: User):
        pass

    @abstractmethod
    def update(self, db: Session, user: User):
        pass
