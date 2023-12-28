from sqlalchemy.orm import Session

import models.user as user_models
import schemas.user as user_schemas
import security.auth as auth_security


def get_user_by_id(db: Session, user_id: int):
    return db.query(user_models.User).filter(user_models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(user_models.User).filter(user_models.User.email == email).first()


def get_user_by_username(db: Session, username: str):
    return (
        db.query(user_models.User).filter(user_models.User.username == username).first()
    )


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(user_models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: user_schemas.UserCreate):
    db_user = user_models.User(
        email=user.email,
        username=user.username,
        hashed_password=auth_security.get_password_hash(user.password),
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int):
    db_user = db.query(user_models.User).filter(user_models.User.id == user_id).first()
    db.delete(db_user)
    db.commit()
    return db_user


def update_user(db: Session, user_id: int, user: user_schemas.UserUpdate):
    db_user = db.query(user_models.User).filter(user_models.User.id == user_id).first()
    if not db_user:
        return None
    db_user.hashed_password = auth_security.get_password_hash(user.password)
    db_user.email = user.email
    db_user.username = user.username
    db.commit()
    db.refresh(db_user)
    return db_user


def authenticate_user(username: str, password: str, db: Session):
    user = get_user_by_username(db, username=username)
    if not user:
        return False
    if not auth_security.verify_password(password, user.hashed_password):
        return False
    return user
