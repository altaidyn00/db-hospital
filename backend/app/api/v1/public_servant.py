from typing import Any
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api import deps
from typing import Optional
from pydantic import BaseModel

router = APIRouter()

class PublicServantBase(BaseModel):
    email: Optional[str] = None
    department: Optional[str] = None

class PublicServantCreate(PublicServantBase):
    email: str
    department: str

class PublicServantUpdate(PublicServantBase):
    pass

# get all public servants
@router.get("/public_servants")
def get_public_servants(
    db: Session = Depends(deps.get_db),
) -> Any:
    try:
        public_servants = db.execute("SELECT * FROM public_servant").fetchall()
        
        return {"public_servants": public_servants}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

# create public servant
@router.post("/public_servants")
def create_public_servant(
    public_servant: PublicServantCreate,
    db: Session = Depends(deps.get_db),
) -> Any:
    try:
        db.execute(
            "INSERT INTO public_servant (email, department) VALUES (:email, :department)",
            params={"email": public_servant.email, "department": public_servant.department},
        )
        db.commit()
        return {"public_servant": public_servant, "message": "Public servant created successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))


# update public servant
@router.put("/public_servants/{email}")
def update_public_servant(
    email: str,
    public_servant: PublicServantUpdate,
    db: Session = Depends(deps.get_db),
) -> Any:
    try:
        db.execute(
            "UPDATE public_servant SET department = :department WHERE email = :email",
            params={"email": email, "department": public_servant.department},
        )
        db.commit()
        return {"public_servant": public_servant, "message": "Public servant updated successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

# delete public servant
@router.delete("/public_servants/{email}")
def delete_public_servant(
    email: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    try:
        db.execute(
            "DELETE FROM public_servant WHERE email = :email",
            params={"email": email},
        )
        db.commit()
        return {"message": "Public servant deleted successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

