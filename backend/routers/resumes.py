from fastapi import APIRouter, HTTPException, UploadFile, File, Form, Depends
from sqlalchemy.orm import Session
from schemas.resume import ResumeCreate, ResumeResponse
from database import get_db
from models.resume import Resume
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

