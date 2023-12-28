import logging
from datetime import datetime, timedelta
from typing import Union

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext

import schemas.auth as auth_schemas
import services.user as user_services
import utils.sql as sql_utils
from utils.env import env

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/token")


def get_password_hash(password: str):
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, env.ACCESS_TOKEN_SECRET_KEY, algorithm=env.ACCESS_TOKEN_ALGORITHM
    )
    return encoded_jwt


def get_current_active_user(
    token: str = Depends(oauth2_scheme), db=Depends(sql_utils.get_db)
):
    # TODO: 在這邊回傳 HTTPException 感覺有點奇怪，看有沒有 middleware 可以用
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            token, env.ACCESS_TOKEN_SECRET_KEY, algorithms=[env.ACCESS_TOKEN_ALGORITHM]
        )

        username = payload.get("sub")

        if username is None:
            raise credentials_exception

        token_data = auth_schemas.TokenData(username=username)
    except JWTError:
        logging.error("JWTError")
        raise credentials_exception
    user = user_services.get_user_by_username(db=db, username=token_data.username)

    if user is None or user.is_active is not True:
        raise credentials_exception

    return user
