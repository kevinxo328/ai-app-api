from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import schemas.user as user_schemas
import security.auth as auth_security
import services.user as user_services
import utils.sql as sql_utils

router = APIRouter(prefix="/users", tags=["users"])

sql_utils.Base.metadata.create_all(bind=sql_utils.engine)


@router.get(
    "",
    response_model=list[user_schemas.User],
    dependencies=[Depends(auth_security.get_current_active_user)],
)
async def get_users(
    skip: int = 0, limit: int = 100, db: Session = Depends(sql_utils.get_db)
):
    try:
        users = user_services.get_users(db, skip=skip, limit=limit)
        return users
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get(
    "/user_id/{id}",
    response_model=user_schemas.User,
    dependencies=[Depends(auth_security.get_current_active_user)],
)
async def get_user_by_id(id: int, db: Session = Depends(sql_utils.get_db)):
    try:
        user = user_services.get_user_by_id(db, user_id=id)
        return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get(
    "/email/{email}",
    response_model=user_schemas.User,
    dependencies=[Depends(auth_security.get_current_active_user)],
)
async def get_user_by_email(email: str, db: Session = Depends(sql_utils.get_db)):
    try:
        user = user_services.get_user_by_email(db, email=email)
        return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/user", response_model=user_schemas.User)
async def create_user(
    user_data: user_schemas.UserCreate, db: Session = Depends(sql_utils.get_db)
):
    try:
        user = user_services.create_user(db, user_data)
        return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.patch(
    "/{user_id}",
    response_model=user_schemas.User,
    dependencies=[Depends(auth_security.get_current_active_user)],
)
async def update_user(
    user_id: int,
    user_data: user_schemas.UserUpdate,
    db: Session = Depends(sql_utils.get_db),
):
    try:
        user = user_services.update_user(db, user_id, user_data)

        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete(
    "/{user_id}",
    response_model=user_schemas.User,
    dependencies=[Depends(auth_security.get_current_active_user)],
)
async def delete_user(user_id: int, db: Session = Depends(sql_utils.get_db)):
    try:
        user = user_services.delete_user(db, user_id)
        return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/current_active_user", response_model=user_schemas.User)
async def get_current_active_user(
    user: Annotated[user_schemas.User, Depends(auth_security.get_current_active_user)]
):
    return user
