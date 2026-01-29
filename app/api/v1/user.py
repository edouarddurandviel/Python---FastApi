from typing import Annotated, List
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.crud import get_all_users, get_one_user, get_filtered_users, create_One_User
from app.schemas import UserResponse, CreateUser
from app.api.deps import postgres_db_session

# router
router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/", response_model=List[UserResponse])
def read_all_users(
    db: Session = Depends(postgres_db_session)
):
    users = get_all_users(db)
    if not users:
                raise HTTPException(status_code=404, detail="User not found")

    return users




@router.get("/search_firstname", response_model=List[UserResponse])
def read_filtered_users(
    firstname: Annotated[str | None, Query(max_length=10)] = None,
    db: Session = Depends(postgres_db_session)
):
    users = get_filtered_users(db, firstname)
    if not users:
            raise HTTPException(status_code=404, detail="User not found")

    return users




@router.get("/{user_Id}", response_model=UserResponse)
def read_one_user(
    user_id: int, 
    with_country: bool = Query(),
    db: Session = Depends(postgres_db_session)
):
    user = get_one_user(db, user_id, with_country)
    if not user:
            raise HTTPException(status_code=404, detail="User not found")

    return user



@router.post("/create", response_model=UserResponse)
def create_one_users(
    user: CreateUser,
    db: Session = Depends(postgres_db_session),
):
    users = create_One_User(db, user)
    if not users:
            raise HTTPException(status_code=404, detail="User not found")

    return users