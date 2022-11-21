from typing import Any
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api import deps
from typing import Optional
from pydantic import BaseModel

router = APIRouter()

class DiscoverBase(BaseModel):
    disease_code: Optional[str] = None
    cname: Optional[str] = None
    first_enc_date: Optional[str] = None

class DiscoverCreate(DiscoverBase):
    disease_code: str
    cname: str
    first_enc_date: str

class DiscoverUpdate(DiscoverBase):
    pass

# get all discoveries
@router.get("/discoveries")
def get_discoveries(
    db: Session = Depends(deps.get_db),
) -> Any:
    try:
        discoveries = db.execute("SELECT * FROM discover").fetchall()
        
        return {"discoveries": discoveries}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

# create discovery
@router.post("/discoveries")
def create_discovery(
    discovery: DiscoverCreate,
    db: Session = Depends(deps.get_db),
) -> Any:
    try:
        db.execute(
            "INSERT INTO discover (disease_code, cname, first_enc_date) VALUES (:disease_code, :cname, :first_enc_date)",
            params={"disease_code": discovery.disease_code, "cname": discovery.cname, "first_enc_date": discovery.first_enc_date},
        )
        db.commit()
        return {"discovery": discovery, "message": "Discovery created successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

# update discovery
@router.put("/discoveries/{disease_code}/{cname}")
def update_discovery(
    disease_code: str,
    cname: str,
    discovery: DiscoverUpdate,
    db: Session = Depends(deps.get_db),
) -> Any:
    try:
        db.execute(
            "UPDATE discover SET first_enc_date = :first_enc_date WHERE disease_code = :disease_code AND cname = :cname",
            params={"disease_code": disease_code, "cname": cname, "first_enc_date": discovery.first_enc_date},
        )
        db.commit()
        return {"discovery": discovery, "message": "Discovery updated successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))


# delete discovery
@router.delete("/discoveries/{disease_code}/{cname}")
def delete_discovery(
    disease_code: str,
    cname: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    try:
        db.execute(
            "DELETE FROM discover WHERE disease_code = :disease_code AND cname = :cname",
            params={"disease_code": disease_code, "cname": cname},
        )
        db.commit()
        return {"message": "Discovery deleted successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
