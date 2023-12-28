from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

import schemas.auth as auth_schemas
import services.user as user_service
import utils.auth as auth_utils
import utils.sql as sql_utils
from utils.env import env

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/token", response_model=auth_schemas.Token)
async def create_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(sql_utils.get_db),
):
    user = user_service.authenticate_user(
        db=db, username=form_data.username, password=form_data.password
    )
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    access_token_expires = timedelta(minutes=env.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth_utils.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/token/refresh")
async def refresh_token():
    pass


@router.post("/logout")
def logout():
    # Your logout logic here
    # ...
    return {"message": "Logged out successfully"}
