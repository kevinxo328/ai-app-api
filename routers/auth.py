from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

import schemas.auth as auth_schemas
import security.oauth2 as oauth2_security
import services.user as user_service
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
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect username or password",
        )

    access_token = oauth2_security.create_token(
        data={"sub": user.username},
        expires_delta=timedelta(minutes=env.ACCESS_TOKEN_EXPIRE_MINUTES),
    )
    refresh_token = oauth2_security.create_token(
        data={"sub": user.username},
        expires_delta=timedelta(minutes=env.REFRESH_TOKEN_EXPIRE_MINUTES),
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "refresh_token": refresh_token,
        "expires_in": env.ACCESS_TOKEN_EXPIRE_MINUTES * 60,
    }


@router.post("/token/refresh", response_model=auth_schemas.Token)
async def refresh_token(refresh_token: str):
    payload = oauth2_security.verify_token(refresh_token)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect username or password",
        )
    access_token = oauth2_security.create_token(
        data={"sub": payload["username"]},
        expires_delta=timedelta(minutes=env.ACCESS_TOKEN_EXPIRE_MINUTES),
    )

    refresh_token = oauth2_security.create_token(
        data={"sub": payload["username"]},
        expires_delta=timedelta(minutes=env.REFRESH_TOKEN_EXPIRE_MINUTES),
    )

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
        "expires_in": env.ACCESS_TOKEN_EXPIRE_MINUTES * 60,
    }


# @router.post("/logout")
# def logout():
#     # Your logout logic here
#     # ...
#     return {"message": "Logged out successfully"}
