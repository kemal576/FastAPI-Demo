from abc import ABC, abstractmethod

from models.abstract.repository import Repository
from models.item import Item


class ItemAbc(Repository, ABC):
    @abstractmethod
    def create(self, item: Item):
        pass

    @abstractmethod
    def update(self, item: Item):
        pass
