from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas import CreateUser, UpdateUser

# CREATE
def create_One_User(db: Session, user: CreateUser):
    db_user = User(
        firstname = user.firstname,
        lastname = user.lastname,
        email = user.email,
        country = user.country
        )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return db_user
    

# READ
def get_all_users(db: Session, skip: int = 0, limit: int = 100):
    users = db.query(User).offset(skip).limit(limit).all()
    db.expire_all()
    return users



def get_filtered_users(db: Session, firstname: str, skip: int = 0, limit: int = 100):
    users = db.query(User).filter(User.firstname == firstname).offset(skip).limit(limit).all()
    db.expire_all()
    return users



def get_one_user(db: Session, id: int, with_country: bool):
      
    if with_country:
        user = db.query(User.firstname, User.country).filter(User.id == id).first()
        db.expire_all()
    else:
        user = db.query(User).filter(User.id == id).first()
        db.expire_all()
        
    return user


# UPDATE
def update_user(db: Session, user_id: int, user: UpdateUser):
    db_user = get_one_user(db, user_id)
    if not db_user:
        return None

    if user.email is not None:
        db_user.email = user.email

    db.commit()
    db.refresh(db_user)
    return db_user



# DELETE
def delete_user(db: Session, user_id: int):
    db_user = get_one_user(db, user_id)
    if not db_user:
        return None
    db.delete(db_user)
    db.commit()
    return db_user