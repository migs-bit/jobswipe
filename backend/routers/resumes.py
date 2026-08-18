from fastapi import APIRouter, HTTPException, UploadFile, File, Form, Depends
from sqlalchemy.orm import Session
from schemas.resume import AnalyzeRequest, AnalyzeResponse, ResumeResponse
from services.resume_tailor import analyze_resume
from database import get_db
from models.resume import Resume
from models.job import Job
from auth import get_current_user
from io import BytesIO
from pypdf import PdfReader
import os

router = APIRouter(prefix="/resumes")

@router.post('/upload', response_model=ResumeResponse, status_code=201)
async def upload_resume(name: str = Form(...), 
                        file: UploadFile = File(...),
                        db: Session = Depends(get_db),
                        current_user = Depends(get_current_user)):

    contents = await file.read()                # wait to read for file and store it as byte code
    reader = PdfReader(BytesIO(contents))       #
    text = ''

    for page in reader.pages:
        text += page.extract_text()

    existing = db.query(Resume).filter(
        Resume.user_id == current_user.id,
        Resume.name == name,
    ).first()

    if existing:
        raise HTTPException(status_code=400, detail='resume already in the system')

    filePath = f"uploads/resumes/user_{current_user.id}_{file.filename}"
    with open(filePath, 'wb') as f:
        f.write(contents)

    new_resume = Resume(
            user_id = current_user.id,
            name = name,
            file_path = filePath,
            raw_text = text
        )

    db.add(new_resume)
    db.commit()
    db.refresh(new_resume)

    return new_resume

@router.post('/{resume_id}/analyze', response_model=AnalyzeResponse, status_code=201)
def analyze(resume_id: int, request: AnalyzeRequest, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    resume = db.query(Resume).filter(
        Resume.id == resume_id,
        Resume.user_id == current_user.id
        ).first()
    
    if not resume:
        raise HTTPException(status_code=404, detail='Resume not found')

    job = db.query(Job).filter(Job.id == request.job_id).first()

    if not job:
        raise HTTPException(status_code=404, detail='Job not found')

    llm_response = analyze_resume(resume.raw_text, job.description)

    return {"suggestions": llm_response}
    