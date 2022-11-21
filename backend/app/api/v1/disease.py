from typing import Any, Optional
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.api import deps

router = APIRouter()


class DiseaseBase(BaseModel):
    disease_code: Optional[str] = None
    description: Optional[str] = None
    pathogen: Optional[str] = None
    id: Optional[int] = None


class DiseaseCreate(DiseaseBase):
    disease_code: str
    description: str
    pathogen: str
    id: int


class DiseaseUpdate(DiseaseBase):
    pass

# get all diseases
@router.get("/diseases")
def get_diseases(
    db: Session = Depends(deps.get_db),
) -> Any:
    try:
        diseases = db.execute("SELECT * FROM disease").fetchall()

        return {"diseases": diseases}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

# create disease
@router.post("/diseases")
def create_disease(
    disease: DiseaseCreate,
    db: Session = Depends(deps.get_db),
) -> Any:
    try:
        db.execute(
            "INSERT INTO disease (disease_code, description, pathogen, id) VALUES (:disease_code, :description, :pathogen, :id)",
            params={"disease_code": disease.disease_code, "description": disease.description,
                    "pathogen": disease.pathogen, "id": disease.id},
        )

        db.commit()

        return {"disease": disease, "message": "Disease created successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

# update disease
@router.put("/diseases/{disease_code}")
def update_disease(
    disease_code: str,
    disease: DiseaseUpdate,
    db: Session = Depends(deps.get_db),
) -> Any:
    try:
        disease = db.execute(
            "UPDATE disease SET disease_code = coalesce(:disease_code, disease_code), description = coalesce(:description, description), pathogen = coalesce(:pathogen, pathogen), id = coalesce(:id, id) WHERE disease_code = :disease_code RETURNING *",
            params={"disease_code": disease.disease_code, "description": disease.description,
                    "pathogen": disease.pathogen, "id": disease.id, "disease_code": disease_code},
        ).fetchone()

        db.commit()

        return {"disease": disease, "message": "Disease updated successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

# delete disease
@router.delete("/diseases/{disease_code}")
def delete_disease(
    disease_code: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    try:
        db.execute(
            "DELETE FROM disease WHERE disease_code = :disease_code",
            params={"disease_code": disease_code},
        )
        db.commit()
        return {"message": "Disease deleted successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
