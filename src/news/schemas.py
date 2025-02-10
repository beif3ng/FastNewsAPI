"""
Pydantic schemas for news app
"""

from datetime import datetime

from pydantic import BaseModel
from typing import List


class CategoryReadSchema(BaseModel):
    """
    Category read schema
    """
    id: int
    name: str
    created: datetime

    class Config:
        orm_mode = True


class CategoryCreateSchema(BaseModel):
    """
    Category create schema
    """
    name: str


class NewsReadSchema(BaseModel):
    """
    News read schema
    """
    id: int
    title: str
    content: str | None = None
    images: List[str] | None = None
    created: datetime
    updated: datetime
    category_id: int | None = None

    class Config:
        orm_mode = True


class NewsCreateSchema(BaseModel):
    """
    News create schema
    """
    title: str
    content: str | None = None
    images: List[str] | None = None
    category_id: int | None = None
