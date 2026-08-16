from database import Base
from sqlalchemy import Integer, Column, Text, String, ForeignKey, DateTime
from datetime import datetime

class Resume(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    name = Column(String, nullable=False)
    file_path = Column(String, nullable=False)
    raw_text = Column(Text, nullable=False)
    uploaded_at = Column(DateTime, default=datetime.utcnow)

