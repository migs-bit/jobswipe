from database import Base
from sqlalchemy import Integer, Column, String, ForeignKey, DateTime
from datetime import datetime
from sqlalchemy import UniqueConstraint

class Swipe(Base):
    __tablename__ = "swipes"                                             #makes this table called Swipe

    id = Column(Integer, primary_key=True, autoincrement=True)          #id for this table data (Swipe)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)   #storing user id to get there info needed for applying and editing resume
    job_id = Column(Integer, ForeignKey("jobs.id"), nullable=False)     # stores jobid to get info easy
    action = Column(String, nullable=False)                             # stores the info on the job card if swiped or not 
    created_at = Column(DateTime, default=datetime.utcnow)              # when the card was swiped on 

    __table_args__ = (UniqueConstraint('user_id', 'job_id'),)