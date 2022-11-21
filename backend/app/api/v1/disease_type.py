from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api import deps

from typing import Optional

from pydantic import BaseModel

router = APIRouter()

class DiseaseTypeBase(BaseModel):
    id: Optional[int] = None
    description: Optional[str] = None

class DiseaseTypeCreate(DiseaseTypeBase):
    description: str

class DiseaseTypeUpdate(DiseaseTypeBase):
    pass

# get all disease types
@router.get("/disease_types")
def get_disease_types(
    db: Session = Depends(deps.get_db),
) -> Any:
    try:
        disease_types = db.execute("SELECT * FROM disease_type").fetchall()
        
        return {"disease_types": disease_types}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

# create disease type
@router.post("/disease_types")
def create_disease_type(
    disease_type: DiseaseTypeCreate,
    db: Session = Depends(deps.get_db),
) -> Any:
    try:
        row = db.execute(
            "INSERT INTO disease_type (description) VALUES (:description) RETURNING id",
            params={"description": disease_type.description},
        ).first()

        db.commit()

        disease_type.id = row.id

        return {"disease_type": disease_type, "message": "Disease type created successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

# update disease type
@router.put("/disease_types/{id}")
def update_disease_type(
    id: int,
    disease_type: DiseaseTypeUpdate,
    db: Session = Depends(deps.get_db),
) -> Any:
    try:
        db.execute(
            "UPDATE disease_type SET description = :description WHERE id = :id",
            params={"id": id, "description": disease_type.description},
        )
        db.commit()

        disease_type.id = id

        return {"disease_type": disease_type, "message": "Disease type updated successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

# delete disease type
@router.delete("/disease_types/{id}")
def delete_disease_type(
    id: int,
    db: Session = Depends(deps.get_db),
) -> Any:
    try:
        db.execute(
            "DELETE FROM disease_type WHERE id = :id",
            params={"id": id},
        )
        db.commit()

        return {"message": "Disease type deleted successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

