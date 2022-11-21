from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api import deps

from typing import Optional

from pydantic import BaseModel

router = APIRouter()

class DoctorBase(BaseModel):
    email: Optional[str] = None
    degree: Optional[str] = None

class DoctorCreate(DoctorBase):
    email: str
    degree: str

class DoctorUpdate(DoctorBase):
    pass

# get all doctors
@router.get("/doctors")
def get_doctors(
    db: Session = Depends(deps.get_db),
) -> Any:
    try:
        doctors = db.execute("SELECT * FROM doctor").fetchall()
        
        return {"doctors": doctors}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

# create doctor
@router.post("/doctors")
def create_doctor(
    doctor: DoctorCreate,
    db: Session = Depends(deps.get_db),
) -> Any:
    try:
        db.execute(
            "INSERT INTO doctor (email, degree) VALUES (:email, :degree)",
            params={"email": doctor.email, "degree": doctor.degree},
        )
        db.commit()
        return {"doctor": doctor, "message": "Doctor created successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

# update doctor
@router.put("/doctors/{email}")
def update_doctor(
    email: str,
    doctor: DoctorUpdate,
    db: Session = Depends(deps.get_db),
) -> Any:
    try:
        db.execute(
            "UPDATE doctor SET degree=:degree WHERE email=:email",
            params={"email": email, "degree": doctor.degree},
        )
        db.commit()
        return {"doctor": doctor, "message": "Doctor updated successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

# delete doctor
@router.delete("/doctors/{email}")
def delete_doctor(
    email: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    try:
        db.execute("DELETE FROM doctor WHERE email=:email", params={"email": email})
        db.commit()
        return {"message": "Doctor deleted successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
