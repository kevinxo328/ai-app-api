from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import schemas.user as user_schemas
import services.user as user_services
import utils.sql as sql_utils

router = APIRouter(prefix="/users", tags=["users"])

sql_utils.Base.metadata.create_all(bind=sql_utils.engine)


@router.get("", response_model=list[user_schemas.User])
async def get_users(
    skip: int = 0, limit: int = 100, db: Session = Depends(sql_utils.get_db)
):
    try:
        users = user_services.get_users(db, skip=skip, limit=limit)
        return users
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/user_id/{id}", response_model=user_schemas.User)
async def get_user_by_id(email: int, db: Session = Depends(sql_utils.get_db)):
    try:
        user = user_services.get_user_by_email(db, email=email)
        return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/email/{email}", response_model=user_schemas.User)
async def get_user_by_email(email: int, db: Session = Depends(sql_utils.get_db)):
    try:
        user = user_services.get_user_by_email(db, email=email)
        return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/users", response_model=user_schemas.User)
def create_user(
    user_data: user_schemas.UserCreate, db: Session = Depends(sql_utils.get_db)
):
    try:
        user = user_services.create_user(db, user_data)
        return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# @router.put("/users/{user_id}")
# def update_user(user_id: int, user_data: dict):
#     # Logic to update a user by ID
#     pass


# @router.delete("/users/{user_id}")
# def delete_user(user_id: int):
#     # Logic to delete a user by ID
#     pass
