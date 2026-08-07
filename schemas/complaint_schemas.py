from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


# -----------------------------
# Create Complaint
# -----------------------------
class ComplaintCreate(BaseModel):

    title: str = Field(..., min_length=5, max_length=200)

    description: str = Field(..., min_length=10)

    category: str

    location: str


# -----------------------------
# Update Complaint
# -----------------------------
class ComplaintUpdate(BaseModel):

    title: str | None = None

    description: str | None = None

    category: str | None = None

    location: str | None = None

    priority: str | None = None

    status: str | None = None

    assigned_to: int | None = None

    remarks: str | None = None


# -----------------------------
# Response Schema
# -----------------------------
class ComplaintResponse(BaseModel):

    id: int

    title: str

    description: str

    category: str

    priority: str

    status: str

    location: str

    image_url: Optional[str]

    student_id: int

    created_at: datetime
    assigned_to: int 
    remarks:str

    class Config:
        from_attributes = True