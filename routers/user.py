from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from repositories.user_repository import UserRepository
from routers.dependencies import get_db
from schemas import user

router = APIRouter()


@router.post("/users/", response_model=user.User)
def create_user(user: user.UserCreate, db: Session = Depends(get_db)):
    db_user = UserRepository.get_user_by_email(db=db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return UserRepository.create(db=db, user=user)


@router.get("/users/{user_id}", response_model=user.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = UserRepository.get(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
