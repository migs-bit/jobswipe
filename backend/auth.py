import bcrypt, jwt
from config.settings import settings
from datetime import datetime, timedelta
from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from models.user import User
from database import get_db
from sqlalchemy.orm import Session

security = HTTPBearer() #creates security scheme for token extraction

def hash_password(password: str) ->str:
    bpwd = password.encode()                #convert pwd to byte
    salt = bcrypt.gensalt()                 #gen salt phrase
    hashpwd = bcrypt.hashpw(bpwd, salt)     #use bcrypt to encrypt pwd with the salt phrase
    return hashpwd.decode()

def verify_password(plain_password: str, hashed_password: str) -> bool:
    #convert plain and hash pwd to byte to compare
    b_plain_pwd = plain_password.encode()
    b_hashed_pwd = hashed_password.encode()
    #checkpw hashes the plain pwd with the same salt from stored hash returns bool 
    is_pwd = bcrypt.checkpw(b_plain_pwd, b_hashed_pwd)
    return is_pwd

def create_access_token(user_id: int, role: str) -> str:
    secret = settings.JWT_SECRET_KEY                            #grab secret key from env file 
    payload = {                                                 #payload = data inside the token
        "user_id": user_id, 
        "role": role,
        "exp": datetime.utcnow() + timedelta(hours=24)
    }
    # encode creates the token by:
    # 1. Putting payload into the middle
    # 2. Creating a signature using secret key
    # 3. Combining into: header.payload.signature
    encoded_jwt=jwt.encode(payload, secret, algorithm=settings.JWT_ALGORITHM)
    return encoded_jwt

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)) ->dict:
    secret = settings.JWT_SECRET_KEY
    token = credentials.credentials                                             #HTTPBearer auto extracts token from auth header
    try:
        payload = jwt.decode(token, secret, algorithms=settings.JWT_ALGORITHM)               #try to decode the client request header by verifying signature
        return payload                                                          #return userid and role
    except jwt.ExpiredSignatureError:                                           
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")


def get_current_user(payload: dict = Depends(verify_token), db: Session = Depends(get_db)) -> User:
    #verify_token extracted user_id from the tokem
    user_id = payload.get("user_id")
    #query the db to grab the actual User obj
    user = db.query(User).filter(User.id == user_id).first()

    #if user doesn't exist anymore, reject
    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    #return actual User obj
    return user             
