from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
import enum
from database import Base
from sqlalchemy import Enum


class User_role(str, enum.Enum):
    teacher = "teacher"
    parent = "parent"
    


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    role = Column(Enum(User_role), nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    
    children = relationship("Student", back_populates="parent", foreign_keys="Student.parent_id")
class Student(Base):
    __tablename__= "students"
    
    id = Column(Integer, primary_key=True, index=True)
    grade = Column(String, nullable=False) # The reason I set the grade column as a string is because
    # Already every studnt will be assigned a grade, I just have to filter it to e.g. grade 12b, grade 12 A
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    
    parent_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    teacher_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    parent = relationship("User", foreign_keys=[parent_id], back_populates="children")
    teacher = relationship("User", foreign_keys=[teacher_id])
    
class Marks(Base):
    __tablename__="marks"
    
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    subject = Column(String, nullable=False)
    test_name = Column(String, nullable=False)
    score = Column(Integer, nullable=False)
    total = Column(Integer, nullable= False)
    date = Column(Date, nullable=False)
    
class BehaviourReport(Base):
    __tablename__ = "behaviourreport"
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    type = Column(String, nullable=False)
    description =  Column(String, nullable=True)
    behaviour_score = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)
    