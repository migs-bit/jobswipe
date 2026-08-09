from fastapi import FastAPI
from routers import jobs, users
from database import engine, Base
from models import job

"""
Base: tracks all models defined
metadata: container obj that keeps together all table def associated with Base
create_all: triggers the actual data definition language generation
engine: database engine that provides connection to db language of my choosing
"""
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(jobs.router, prefix='/api/v1')
app.include_router(users.router, prefix='/api/v1')

@app.get("/")
def home():
    return {"status": "running", "app": "JobSwipe"}