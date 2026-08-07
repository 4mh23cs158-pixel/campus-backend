from pydantic import BaseModel, EmailStr
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DepartmentCreate(BaseModel):

    department_name: str

    department_email: EmailStr

    department_phone: str


class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True)

    department_name = Column(String(100), unique=True, nullable=False)
    department_email = Column(String(100), nullable=False)
    department_phone = Column(String(10), nullable=False)
    complaints = relationship("Complaint", back_populates="department")
    phone_number = Column(String(10), nullable=False)

    description = Column(Text, nullable=True)

class DepartmentResponse(BaseModel):

    id: int

    department_name: str

    department_email: EmailStr

    department_phone: str

    class Config:
        from_attributes = True