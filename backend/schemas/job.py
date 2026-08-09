from pydantic import BaseModel, field_validator
from typing import Optional, Any

class JobResponse(BaseModel):
    id: int
    title: str
    company: str
    location: str
    salary: str
    description: str
    tags: Optional[list[str]] = []

    @field_validator('tags', mode='before')
    @classmethod
    def tokenizing_tags(cls, value: Any ) -> list:
        if value is None:
            return []
        if isinstance(value, str):
            return value.split(',')
        return []


    class Config:
        from_attributes = True

class JobCreate(BaseModel):
    title: str
    company: str
    location: str
    salary: str
    description: str