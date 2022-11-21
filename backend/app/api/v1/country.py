from typing import Any
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api import deps
from typing import Optional
from pydantic import BaseModel

router = APIRouter()


class CountryBase(BaseModel):
    cname: Optional[str] = None
    population: Optional[int] = None

class CountryCreate(CountryBase):
    cname: str
    population: int

class CountryUpdate(CountryBase):
    pass

# get all countries
@router.get("/countries")
def get_countries(
    db: Session = Depends(deps.get_db),
) -> Any:
    try:
        countries = db.execute("SELECT * FROM country").fetchall()
        
        return {"countries": countries}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

# create country
@router.post("/countries")
def create_country(
    country: CountryCreate,
    db: Session = Depends(deps.get_db),
) -> Any:
    try:
        db.execute(
            "INSERT INTO country (cname, population) VALUES (:cname, :population)",
            params={"cname": country.cname, "population": country.population},
        )
        db.commit()
        return {"country": country, "message": "Country created successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))


# update country
@router.put("/countries/{cname}")
def update_country(
    cname: str,
    country: CountryUpdate,
    db: Session = Depends(deps.get_db),
) -> Any:
    try:
        country = db.execute(
            "UPDATE country SET cname = COALESCE(:cname, cname), population = COALESCE(:population, population) WHERE cname = :cname RETURNING *",
            params={"cname": cname, "population": country.population},
        ).fetchone()

        db.commit()
            
        return {"country": country, "message": "Country updated successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

# delete country
@router.delete("/countries/{cname}")
def delete_country(
    cname: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    try:
        db.execute("DELETE FROM country WHERE cname=:cname", params={"cname": cname})
        db.commit()
        return {"message": "Country deleted successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
