from typing import List, Optional

from pydantic import BaseModel, Field

class Comment(BaseModel):
    item_id: int
    name: str
    description: str


    class Config:
        orm_mode = True

class CommentCreate(BaseModel):
    name: str = Field(max_length=100)
    description: str 
    image_id: int = Field(gt=0, lt=7)
