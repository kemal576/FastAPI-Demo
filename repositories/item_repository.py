from sqlalchemy.orm import Session
from models.item import Item
from schemas.item import ItemCreate


class ItemRepository:
    @classmethod
    def get(cls, db: Session, item_id: int):
        return db.query(Item).filter(Item.id == item_id).first()

    @classmethod
    def get_by_owner_id(cls, db: Session, owner_id: int):
        return db.query(Item).filter(Item.owner_id == owner_id).all()

    @classmethod
    def get_all(cls, db: Session):
        return db.query(Item).all()

    @classmethod
    def create(cls, db: Session, item: ItemCreate, owner_id: int):
        db_item = Item(title=item.title, description=item.description, owner_id=owner_id)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item

    @classmethod
    def delete(cls, db: Session, user: Item):
        db.delete(user)
        db.commit()
