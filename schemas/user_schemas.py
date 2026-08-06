from pydantic import BaseModel, EmailStr, Field

class UserBase(BaseModel):
    name: str
    email: str
    password: str
    phone_number: str = Field(..., min_length=10, max_length=15)

class Userlogin(BaseModel):
    email: str
    password: str