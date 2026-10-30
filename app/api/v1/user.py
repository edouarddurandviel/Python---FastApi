from typing import Annotated, List
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.crud import getAllUsers, getOneUser, getFilteredUsers, createOneUser
from app.schemas import UserResponse, CreateUser
from app.api.deps import postgresDbSession

# router
router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/", response_model=List[UserResponse])
def getAllUsers(
    db: Session = Depends(postgresDbSession)
):
    users = getAllUsers(db)
    if not users:
                raise HTTPException(status_code=404, detail="Users not found")

    return users




@router.get("/search_firstname", response_model=List[UserResponse])
def getFilteredUsers(
    firstname: Annotated[str | None, Query(max_length=10)] = None,
    db: Session = Depends(postgresDbSession)
):
    users = getFilteredUsers(db, firstname)
    if not users:
            raise HTTPException(status_code=404, detail="User not found")

    return users




@router.get("/{user_Id}", response_model=UserResponse)
def readOneUser(
    user_id: Annotated[int | None, Query(max_digits=3)] = None, 
    with_country: bool = Query(),
    db: Session = Depends(postgresDbSession)
):
    user = getOneUser(db, user_id, with_country)
    if not user:
            raise HTTPException(status_code=404, detail="User not found")

    return user



@router.post("/create", response_model=UserResponse)
def createOneUser(
    user: CreateUser,
    db: Session = Depends(postgresDbSession),
):
    users = createOneUser(db, user)
    if not users:
            raise HTTPException(status_code=400, detail="Bad Request: could not create User")

    return users