from typing import Any
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api import deps
from typing import Optional
from pydantic import BaseModel

router = APIRouter()
class RecordBase(BaseModel):
    email: Optional[str] = None
    disease_code: Optional[str] = None
    cname: Optional[str] = None
    total_deaths: Optional[int] = None
    total_patients: Optional[int] = None

class RecordCreate(RecordBase):
    cname: str
    email: str
    disease_code: str
    total_deaths: int
    total_patients: int

class RecordUpdate(RecordBase):
    total_deaths: Optional[int]
    total_patients: Optional[int]

# get all records
@router.get("/records")
def get_records(
    db: Session = Depends(deps.get_db),
) -> Any:
    try:
        records = db.execute("SELECT * FROM record").fetchall()
        
        return {"records": records}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

# create record
@router.post("/records")
def create_record(
    record: RecordCreate,
    db: Session = Depends(deps.get_db),
) -> Any:
    try:
        db.execute(
            "INSERT INTO record (cname, email, disease_code, total_deaths, total_patients) VALUES (:cname, :email, :disease_code, :total_deaths, :total_patients)",
            params={"cname": record.cname, "email": record.email, "disease_code": record.disease_code, "total_deaths": record.total_deaths, "total_patients": record.total_patients},
        )
        db.commit()
        return {"record": record, "message": "Record created successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

# update record
@router.put("/records/{email}/{cname}/{disease_code}")
def update_record(
    cname: str,
    disease_code: str,
    email: str,
    record: RecordUpdate,
    db: Session = Depends(deps.get_db),
) -> Any:
    try:
        db.execute(
            "UPDATE record SET total_deaths=:total_deaths, total_patients=:total_patients WHERE cname=:cname AND disease_code=:disease_code AND email=:email",
            params={"cname": cname, "disease_code": disease_code, "email": email, "total_patients": record.total_patients, "total_deaths": record.total_deaths},
        )
        db.commit()
        return {"record": record, "message": "Record updated successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

# delete record
@router.delete("/records/{email}/{cname}/{disease_code}")
def delete_record(
    cname: str,
    disease_code: str,
    email: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    try:
        db.execute("DELETE FROM record WHERE cname=:cname AND disease_code=:disease_code AND email=:email", params={"cname": cname, "disease_code": disease_code, "email": email})
        db.commit()
        return {"message": "Record deleted successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))



