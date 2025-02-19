"""
Pydantic schemas for Comment
"""

from datetime import datetime

from pydantic import BaseModel

from .news import NewsReadSchema


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


class CommentReadDetailsSchema(BaseModel):
    """
    Comment read details schema with detailed news data
    """
    comment: NewsReadSchema
