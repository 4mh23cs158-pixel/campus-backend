from db import Base
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from datetime import datetime

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    phone_number=Column(String(10), nullable=False)
    role=Column(String(20), default="student")
    complaints = relationship("Complaint", back_populates="student")

class Complaint(Base):
    __tablename__ = "complaints"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(200), nullable=False)

    description = Column(Text, nullable=False)

    category = Column(
    String(100),
    nullable=False
)

    department_id = Column(
    Integer,
    ForeignKey("departments.id"),
    nullable=True
)

    department = relationship(
    "Department",
    back_populates="complaints"
)

    priority = Column(
        String(20),
        default="Low"
    )
    status = Column(
        String(30),
        default="Pending"
    )
    location = Column(
        String(200),
        nullable=False
    )

    image_url = Column(
        String(300),
        nullable=True
    )

    assigned_to =Column(
        Integer,
        nullable=True
    )

    remarks = Column(
        Text,
        nullable=True
    )
    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    student_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    student = relationship(
    "User",
        back_populates="complaints"
    )

class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True)

    department_name = Column(String(100), unique=True, nullable=False)
    department_email = Column(String(100), nullable=False)
    department_phone = Column(String(10), nullable=False)
    complaints = relationship("Complaint", back_populates="department")


    description = Column(Text, nullable=True)