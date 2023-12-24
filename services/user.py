from sqlalchemy.orm import Session

import models.user as user_models
import schemas.user as user_schemas


def get_user_by_id(db: Session, user_id: int):
    return db.query(user_models.User).filter(user_models.User.id == user_id).first()


def get_user_by_email(db: Session, email: int):
    return db.query(user_models.User).filter(user_models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(user_models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: user_schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = user_models.User(
        email=user.email, username=user.username, hashed_password=fake_hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
