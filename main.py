from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import models, schemas 
from Authentication import hashPassword

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.post("/users", response_model=schemas.UserResponse)   
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # The magic of hashing every password a user creates, even if my backend could get hacked, passwords are hashed.
    hashed_password = hashPassword(user.password)   