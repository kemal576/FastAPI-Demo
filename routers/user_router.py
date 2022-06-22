from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status
from repositories.item_repository import ItemRepository
from repositories.user_repository import UserRepository
from routers.dependencies import get_db
from schemas.user import User, UserCreate
from schemas.item import ItemCreate, Item

router = APIRouter(prefix="/users")


@router.post("/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = UserRepository.get_user_by_email(db=db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered!")
    return UserRepository.create(db=db, user=user)


@router.post("/{user_id}/items", response_model=Item)
def create_user_item(user_id: int, item: ItemCreate, db: Session = Depends(get_db)):
    db_user = UserRepository.get(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Owner not found.")
    return ItemRepository.create(db, item, user_id)


@router.get("/", response_model=list[User])
def get_all(db: Session = Depends(get_db)):
    db_users = UserRepository.get_all(db)
    if db_users is None:
        raise HTTPException(status_code=404, detail="Users not found.")
    return db_users


@router.get("/{user_id}", response_model=User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = UserRepository.get(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.delete("/{user_id}", response_model=User, status_code=status.HTTP_200_OK)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = UserRepository.get(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    UserRepository.delete(db, db_user)
