from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api import deps

from typing import Optional

from pydantic import BaseModel

router = APIRouter()

class UserBase(BaseModel):
    name: Optional[str] = None
    surname: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    salary: Optional[int] = None
    cname: Optional[str] = None

class UserCreate(UserBase):
    name: str
    surname: str
    email: str
    phone: str
    salary: int
    cname: str

class UserUpdate(UserBase):
    pass

# get all users
@router.get("/users")
def get_users(
    db: Session = Depends(deps.get_db),
) -> Any:
    try:
        users = db.execute("SELECT * FROM users").fetchall()
        
        return {"users": users}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

# create user
@router.post("/users")
def create_user(
    user: UserCreate,
    db: Session = Depends(deps.get_db),
) -> Any:
    try:
        db.execute(
            "INSERT INTO users (name, surname, email, phone, salary, cname) VALUES (:name, :surname, :email, :phone, :salary, :cname)",
            params={"name": user.name, "surname": user.surname, "email": user.email, "phone": user.phone, "salary": user.salary, "cname": user.cname},
        )
        db.commit()
        return {"user": user, "message": "User created successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))


# update user
@router.put("/users/{email}")
def update_user(
    email: str,
    user: UserUpdate,
    db: Session = Depends(deps.get_db),
) -> Any:
    try:
        # update using coallesce to avoid null values and returning
        user = db.execute(
            "UPDATE users SET name = COALESCE(:name, name), surname = COALESCE(:surname, surname), phone = COALESCE(:phone, phone), salary = COALESCE(:salary, salary), cname = COALESCE(:cname, cname) WHERE email = :email RETURNING *",
            params={"name": user.name, "surname": user.surname, "email": email, "phone": user.phone, "salary": user.salary, "cname": user.cname},
        ).fetchone()

        return {"user": user, "message": "User updated successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

# delete user
@router.delete("/users/{email}")
def delete_user(
    email: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    try:
        db.execute(
            "DELETE FROM users WHERE email = :email",
            params={"email": email},
        )
        db.commit()
        return {"message": "User deleted successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))


    