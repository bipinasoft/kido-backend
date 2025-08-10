from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    created_at: datetime
    class Config:
        orm_mode = True

class ActivityBase(BaseModel):
    title: str
    description: Optional[str]
    difficulty_level: Optional[str]

class ActivityCreate(ActivityBase):
    pass

class Activity(ActivityBase):
    id: int
    created_at: datetime
    class Config:
        orm_mode = True

class ProgressBase(BaseModel):
    user_id: int
    activity_id: int
    score: int

class ProgressCreate(ProgressBase):
    pass

class Progress(ProgressBase):
    id: int
    completed_at: datetime
    class Config:
        orm_mode = True
