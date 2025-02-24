"""
Services module contains business logic
"""


from typing import Sequence

from fastapi import HTTPException

from sqlalchemy.ext.asyncio import AsyncSession

from . import CategoryService
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
        if comment is None:
            raise HTTPException(status_code=404, detail="Comment not found")
        return comment


    @classmethod
    async def create_comment(
            cls,
            db: AsyncSession,
            comment: dict
    ) -> Comment:
        """
        Service
        """

        return await DBManager.create_object(**comment, db=db, model=Comment, commit=True)


    @classmethod
    async def delete_comment(
            cls,
            db: AsyncSession,
            comment_id: int,
    ) -> None:
        """
        Service
        """
        await DBManager.delete_object(db=db, model=Comment, field="id", value=comment_id, commit=True)

    @classmethod
    async def update_comment(
            cls,
            db: AsyncSession,
            comment_id: int,
            comment: dict,
            partial: bool = False,
    ) -> Comment:
        """
        Service
        """
        if partial:
            comment = await DBManager.partial_update_object(**comment,db=db, model=Comment, field="id",
                                                            value=comment_id, commit=True)
        else:
            comment = await DBManager.update_object(**comment, db=db, model=Comment, field="id",
                                                     value=comment_id, commit=True)

        if comment is None:
            raise HTTPException(status_code=404, detail="Comment not found")
        return comment










