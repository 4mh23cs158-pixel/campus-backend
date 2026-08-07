from pydantic import BaseModel, EmailStr, Field

class UserBase(BaseModel):
    name: str
    email: str
    password: str
    phone_number: str = Field(..., min_length=10, max_length=15)
    role: str = "student"
class Userlogin(BaseModel):
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone_number: str
    role: str

    class Config:
        from_attributes = True

class UserUpdate(BaseModel):
    name: str | None = None
    phone_number: str | None = Field(None, min_length=10, max_length=15)