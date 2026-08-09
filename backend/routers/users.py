from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas.user import UserResponse, UserCreate, LoginRequest
from database import get_db
from auth import hash_password, verify_password
from models.user import User

router = APIRouter(prefix='/users')

@router.post("/register", response_model=UserResponse, status_code=201)
def create_user(user: UserCreate, db: Session=Depends(get_db)):
    existing = db.query(User).filter(User.email==user.email).first()
    if existing:
        raise HTTPException(status_code = 400, detail="Email already registered")
    
    hash_pwd = hash_password(user.password)
    new_user = User(
    email=user.email,
    username=user.username,
    hashed_password=hash_pwd
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.post("/login", response_model=UserResponse, status_code=200)
def request_login(user: LoginRequest, db: Session=Depends(get_db)):
    existing=db.query(User).filter(User.email==user.email).first()
    if not existing :
        raise HTTPException(status_code=401, detail="Incorrect email or password, Try Again")


    pwd_check = verify_password(user.password, existing.hashed_password)
    if not pwd_check:
        raise HTTPException(status_code=401, detail="Incorrect email or password, Try Again")

    return existing
    