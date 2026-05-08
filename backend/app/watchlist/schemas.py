from pydantic import BaseModel

class WatchCreate(BaseModel):
    title: str
    author: str | None = None


class WatchResponse(BaseModel):
    id: int
    title: str
    author: str | None

    class Config:
        from_attributes = True
