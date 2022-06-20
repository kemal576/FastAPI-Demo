from abc import ABC, abstractmethod
import uuid

from sqlalchemy.orm import Session


class Repository(ABC):
    @abstractmethod
    def get(self, db: Session, uuid: uuid):
        pass

    @abstractmethod
    def create(self, db: Session, object: object):
        pass

    @abstractmethod
    def update(self, db: Session, object: object):
        pass

    @abstractmethod
    def delete(self, db: Session, uuid: uuid):
        pass
