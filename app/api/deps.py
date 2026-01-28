from typing import Generator
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import SessionLocal

def postgres_db_session() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def is_user_authenticated():
    # placeholder for JWT / OAuth
    
    
    user = None
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
        )
    return user