from pydantic import BaseModel
from datetime import date




class UserBase(BaseModel):
    first_name: str
    last_name: str
    role: str
    email: str
    

class UserCreate(UserBase):
    password: str # Basically in here it is the input for plain passwords and it is only used when signing up
    
class UserResponse(UserBase):
    id: int

    
class StudentBase(BaseModel):
    grade:str
    first_name: str
    last_name: str
    parent_id: int
    teacher_id:int
    
class BehaviourReportBase(BaseModel):
    student_id: int
    type: str
    description: str
    behaviour_score: int
    date: date
    
class MarksBase(BaseModel):
    student_id: int
    subject: str
    test_name: str
    score: int
    total: int
    date: date