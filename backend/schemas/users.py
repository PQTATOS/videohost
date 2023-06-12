from pydantic import BaseModel, Field, EmailStr, UUID4


class UserCreate(BaseModel):
    email: EmailStr
    username: str
    hashed_password: str = Field(alias="password")


class UserShow(BaseModel):
    id: int
    email: EmailStr
    username: str
    is_active: bool

