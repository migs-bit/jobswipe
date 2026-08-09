from database import SessionLocal
from models.job import Job

jobs = [
        {"title": "jr software engineer", "company": "Google", "location": "San Francisco","salary": "80k-120k", "description": "your gonna be coding bro, $35/hour", "tags": "DSA, Python, Kupernetizes" },
        {"title": "developer intern", "company": "Tik Tok", "location": "Houston","salary": "competitive", "description": "your gonna be coding bro, $20/hour", "tags": "DSA, Python, Kupernetizes" },
        {"title": "data anaylst", "company": "Amazon", "location": "New York City","salary": "DOE", "description": "your gonna be coding bro, $45/hour", "tags": "DSA, Python, Kupernetizes" },
        {"title": "SW engineering intern", "company": "Roblox", "location": "Los Angeles","salary": "$150,000 - $200,000", "description": "your gonna be coding bro, $60/hour", "tags": "DSA, Python, Kupernetizes" }
    ]

db = SessionLocal()

try:
    if db.query(Job).first():
        print("Database already seeded, skipping")
        db.close()
        exit()
    job_instance = [Job(**row) for row in jobs]
    db.add_all(job_instance)
    db.commit()
finally:
    db.close()