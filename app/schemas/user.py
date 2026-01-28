# Data validation: pydantic
###########################
from typing import Optional
from pydantic import BaseModel

# user extends base
class UserBase(BaseModel):
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    email: Optional[str] = None
    country: Optional[int] = None
    
class CreateUser(UserBase):
    firstname: str
    lastname: str
    email: str
    country: int

class UpdateUser(BaseModel):
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    email: Optional[str] = None
    country: Optional[int] = None


class UserResponse(UserBase):
    id: int
    
    class Config:
        orm_mode: True # Alchemy compat.
    
