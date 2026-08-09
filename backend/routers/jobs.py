from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas.job import JobResponse, JobCreate
from database import get_db
from models.job import Job

router = APIRouter(prefix="/jobs")

#Query is manipulation of data from a database table, add,delete,edit table

@router.get("/",response_model=list[JobResponse])
def getJobList(db: Session = Depends(get_db)):
    jobs = db.query(Job).all()
    return jobs

@router.get("/{id}", response_model=JobResponse)
def getSingleJob(id: int, db: Session = Depends(get_db)):
    job = db.query(Job).filter(Job.id == id).first()
    if not job:
        raise HTTPException(status_code=404, detail="ID was not found")
    return job

@router.post("/", response_model=JobResponse, status_code=201)
def createJob(job: JobCreate, db: Session = Depends(get_db)):
    new_job = Job(**job.model_dump())
    db.add(new_job)
    db.commit()
    db.refresh(new_job)
    return new_job
 

