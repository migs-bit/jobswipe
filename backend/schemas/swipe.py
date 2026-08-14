from pydantic import BaseModel, field_validator
from datetime import datetime
from typing import Optional, Any

class SwipeCreate(BaseModel):
    job_id: int
    action: str

    field_validator("action")
    @classmethod
    def valid_action(cls, v):
        allowed = {'pass', 'save', 'apply', 'skip'}
        if v not in allowed:
            raise ValueError(f"action must be one of {allowed}")
        return v

class SwipeResponse(BaseModel):
    id: int
    user_id: int
    job_id: int
    action: str
    created_at: datetime

    class Config:
        from_attributes = True