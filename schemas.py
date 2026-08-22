from pydantic import BaseModel
import datetime as Datetime


class UserBase(BaseModel):
    full_name: str
    last_name: str
    role: str
    email: str
    hashed_password: str
    
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
    date: Datetime
    
class MarksBase(BaseModel):
    student_id: int
    subject: str
    test_name: str
    score: int
    total: int
    date: Datetime