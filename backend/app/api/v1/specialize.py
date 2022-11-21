from typing import Any
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api import deps
from typing import Optional
from pydantic import BaseModel

router = APIRouter()

class SpecializeBase(BaseModel):
    email: Optional[str] = None
    id: Optional[int] = None

class SpecializeCreate(SpecializeBase):
    email: str
    id: int

class SpecializeUpdate(SpecializeBase):
    pass


# get all specializes
@router.get("/specializes")
def get_specializes(
    db: Session = Depends(deps.get_db),
) -> Any:
    try:
        specializes = db.execute("SELECT * FROM specialize").fetchall()
        
        return {"specializes": specializes}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

# create specialize
@router.post("/specializes")
def create_specialize(
    specialize: SpecializeCreate,
    db: Session = Depends(deps.get_db),
) -> Any:
    try:
        db.execute(
            "INSERT INTO specialize (email, id) VALUES (:email, :id)",
            params={"email": specialize.email, "id": specialize.id},
        )

        db.commit()

        return {"specialize": specialize, "message": "Specialize created successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

# delete specialize
@router.delete("/specializes/{email}/{id}")
def delete_specialize(
    email: str,
    id: int,
    db: Session = Depends(deps.get_db),
) -> Any:
    try:
        db.execute(
            "DELETE FROM specialize WHERE email = :email AND id = :id",
            params={"email": email, "id": id},
        )

        db.commit()

        return {"message": "Specialize deleted successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))


        



