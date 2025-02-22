"""
Services module contains business logic
"""


from typing import Sequence

from fastapi import HTTPException

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from ..models import Comment

from src.manager import DBManager


class CommentService:

    @classmethod
    async def get_comments(
        cls,
        db: AsyncSession,
        offset: int = 0,
        limit: int = 10,
    ) -> Sequence[Comment]:
        """
        Service
        """
        return await DBManager.get_objects(db, model=Comment, offset=offset, limit=limit)


    @classmethod
    async def get_comment(
        cls,
        db: AsyncSession,
        comment_id: int,
    ) -> Comment:
        """
        Service
        """
        comment = await DBManager.get_object(db=db, model=Comment, field="id", value=comment_id)






















