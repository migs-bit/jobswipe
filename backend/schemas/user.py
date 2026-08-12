from pydantic import BaseModel, field_validator
from datetime import datetime
from typing import Optional, Any

class UserResponse(BaseModel):
    id: int
    email: str
    username: str
    role: str
    is_active: bool
    created_at: Optional[datetime] = None


    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    email: str
    username: str
    password: str

    @field_validator('password')
    @classmethod
    def validate_password(cls, v):
        if len(v) < 8:
            raise ValueError('password must be atleast 8 characters')
        return v

class LoginRequest(BaseModel):
    email: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str