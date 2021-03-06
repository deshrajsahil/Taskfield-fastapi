from pydantic import BaseModel
from datetime import date
from typing import List, Optional

from sqlalchemy import false


class UserBase(BaseModel):
  username: str
  email: str
  password: str

# for user display
class UserDisplay(BaseModel):
  username: str
  email: str
  class Config():
    orm_mode = True

class TodoBase(BaseModel):
  task: str
  assigned_to: str
  due_date: date
  is_completed: Optional[bool]='false'
  creator_id: Optional[int] = ''
  grp_txt: Optional[str] = ''
  grp_id: Optional[int] = ''

# For user who assigned task Display
class User(BaseModel):
  username: str
  class Config():
    orm_mode = True

# for todo display
class TodoDisplay(BaseModel):
  id: int
  task: str
  assigned_to: str
  due_date: date
  is_completed: bool
  grp_txt: str
  grp_id: int
  # user: User
  class Config():
    orm_mode = True

class UserAuth(BaseModel):
  id: int
  username: str
  email: str


# update todo
class Update_TodoBase(BaseModel):
  id: int
  task: str
  assigned_to: str
  due_date: str
  is_completed: bool
  creator_id: int


class Update_TodoDisplay(BaseModel):
  id: int
  task: str
  assigned_to: str
  due_date: str
  is_completed: bool
  creator_id: int
  class Config():
    orm_mode = True

