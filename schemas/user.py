import uuid

from pydantic import BaseModel, EmailStr, field_validator


class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserPassword(BaseModel):
    password: str

    # Define a validator for the password field
    @field_validator("password")
    def check_password(cls, value):
        # convert the password to a string if it is not already
        value = str(value)
        # check that the password has at least 8 characters, one uppercase letter,
        # one lowercase letter, and one digit
        if len(value) < 8:
            raise ValueError("Password must have at least 8 characters")
        if not any(c.isupper() for c in value):
            raise ValueError("Password must have at least one uppercase letter")
        if not any(c.islower() for c in value):
            raise ValueError("Password must have at least one lowercase letter")
        if not any(c.isdigit() for c in value):
            raise ValueError("Password must have at least one digit")
        return value


class UserCreate(UserBase, UserPassword):
    pass


class User(UserBase):
    id: uuid.UUID
    is_active: bool

    class Config:
        from_attributes = True


class UserUpdate(UserBase, UserPassword):
    pass
