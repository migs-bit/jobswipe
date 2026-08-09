from database import Base
from sqlalchemy import Integer, Column, String, Text

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    company = Column(String, nullable=False)
    location = Column(String)
    salary = Column(String)
    description = Column(Text)
    tags = Column(String(256))