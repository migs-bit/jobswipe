import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    #database
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./jobswipe.db")

    #jwt auth
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    JWT_ALGORITHM = "HS256"
    JWT_EXPIRED_HOURS = 24

    #llm 
    DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
    DEEPSEEK_BASE_URL = os.getenv("DEEPSEEK_BASE_URL")

    #file upload
    UPLOAD_DIR = "uploads/resumes"

settings = Settings()