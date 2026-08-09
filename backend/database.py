from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#specifing where the database lives and what type it is, dont need to change code when changing database systems
DATABASE_URL = "sqlite:///./jobswipe.db"
# allows for a connection pool of sessions without needing to make new ones, lazy evaluates connections 
engine = create_engine(DATABASE_URL)
#manages connection pool
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#creates base class that database models will inherit from
Base = declarative_base()

#generator that yields db for a session when called and can query data until method using this call exits 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



