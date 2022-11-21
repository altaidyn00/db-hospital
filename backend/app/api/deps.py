# deps file
from app.engine import SessionLocal
from typing import Generator
from fastapi import Depends
from sqlalchemy.orm import Session

def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()




