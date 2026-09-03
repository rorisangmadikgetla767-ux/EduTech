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
    new_user = models.User(
        first_name=user.first_name,
        last_name=user.lastname,
        role=user.role,
        email=user.email,
        hashed_password=hashPassword
    )  
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post("/students", response_model=schemas.StudentBase)
def create_student(student: schemas.StudentBase, db:Session = Depends(get_db)):
    new_student = models.Student(
        grade = student.grade,
        first_name = student.first_name,
        last_name = student.last_name,
        parent_id = student.parent_id,
        teacher_id = student.teacher_id
    )
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student
@router.post("/marks", response_model=schemas.MarksBase)
def add_marks(marks: schemas.MarksBase, db:Session = Depends(get_db)):
    new_marks = models.Marks(
        student_id = marks.student_id,
        subject = marks.subject,
        test_name = marks.test_name,
        score = marks.score,
        total = marks.total,
        date = marks.date           
    )
    db.add(new_marks)
    db.commit()
    db.refresh(new_marks)
    return new_marks

# This is the log-in endpoint
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
import models, schemas
from Authentication import verify_password, create_access_token

@router.post("/login")
def login(credentials: schemas.LoginRequest, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == credentials.email).first()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email / Invalid password"
        )
        
    if not verify_password(credentials.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email / Invalid password"
        )
        
    
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}