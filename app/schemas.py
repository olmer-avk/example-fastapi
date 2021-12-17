from pydantic import BaseModel, EmailStr, conint
from datetime import datetime
from typing import Optional


class UserBase(BaseModel):
    email: EmailStr
    password: str


class UserCreate(UserBase):
    pass


class UserLogin(UserBase):
    pass


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    create_at: datetime

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int
    create_at: datetime
    owner_id: int
    owner: UserResponse

    class Config:
        orm_mode = True


class PostResponse(BaseModel):
    Post: Post
    votes: int

    class Config:
        orm_mode = True


class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)
