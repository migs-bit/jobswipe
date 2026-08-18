from pydantic import BaseModel, field_validator
from datetime import datetime
from typing import Optional, Any

class ResumeCreate(BaseModel):
    name: str

class ResumeResponse(BaseModel):
    id: int
    user_id: int
    name: str
    file_path: str
    raw_text: str
    uploaded_at: datetime

    class Config:
        from_attributes = True

class AnalyzeRequest(BaseModel):
    job_id: int

class AnalyzeResponse(BaseModel):
    suggestions: str