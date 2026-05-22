from pydantic import BaseModel
from typing import Literal


class BookCreate(BaseModel):
    title: str
    author: str | None = None
    category: Literal["lend","sell"]


class BookResponse(BaseModel):
    id: int
    title: str
    author: str | None
    category: str
    owner_id: int

    class Config:
        orm_mode = True
        from_attributes = True
