"""
Pydantic schemas for news app
"""

from datetime import datetime

from pydantic import BaseModel
from typing import Optional, List


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
    content: Optional[str] = None
    images: Optional[List[str]] = None
    created: datetime
    updated: datetime
    category_id: Optional[int] = None

    class Config:
        orm_mode = True


class NewsCreateSchema(BaseModel):
    """
    News create schema
    """
    title: str
    content: Optional[str] = None
    images: Optional[List[str]] = None
    category_id: Optional[int] = None
