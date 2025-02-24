"""
Pydantic schemas for Comment
"""

from datetime import datetime

from pydantic import BaseModel


class CommentReadSchema(BaseModel):
    """
    Comment read schema
    """
    id: int
    text: str
    created: datetime
    updated: datetime
    news_id: int

    class Config:
        from_attributes = True


class CommentCreateSchema(BaseModel):
    """
    Comment create schema
    """
    news_id: int
    text: str


