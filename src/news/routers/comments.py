"""
Comments router
"""

from typing import Sequence, Annotated

from fastapi import APIRouter, Depends, Form, File, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_db

from ..services import CommentService
from ..schemas import CommentReadSchema, CommentCreateSchema
from ..models import Comment


router = APIRouter(
    prefix="/comments",
    tags=["Comment"]
)


@router.get("", response_model=Sequence[CommentReadSchema])
async def get_comments(offset: int = 0, limit:int = 10, db: AsyncSession = Depends(get_db)) -> Sequence[Comment]:
    """
    Get all comments
    """
    return await CommentService.get_comments(db, offset=offset, limit=limit)



@router.get("/{comment_id}", response_model=CommentReadSchema)
async def get_comment(comment_id: int, db: AsyncSession = Depends(get_db)) -> Comment:
    """
    Get comment by id
    """
    return await CommentService.get_comment(db, comment_id)


@router.post("/{comment_id}", response_model=CommentReadSchema)
async def create_comment(comment: CommentCreateSchema, db: AsyncSession = Depends(get_db)) -> Comment:
    """
    Create comment
    """
    return await CommentService.create_comment(db, comment.dict())


@router.delete("/{comment_id}", status_code=204)
async def delete_comment(comment_id: int, db: AsyncSession = Depends(get_db)) -> None:
    """
    Delete comment by id
    """
    return await CommentService.delete_comment(db, comment_id)


@router.put("/{comment_id}", response_model=CommentReadSchema)
async def update_comment(comment_id: int, comment: CommentCreateSchema, db: AsyncSession = Depends(get_db)) -> Comment:
    """
    Update comment by id
    """
    return await CommentService.update_comment(db, comment_id, comment.dict())


@router.patch("/{comment_id}", response_model=CommentReadSchema)
async def partial_update_comment(comment_id: int, comment: CommentCreateSchema, db: AsyncSession = Depends(get_db)) -> Comment:
    """
    Update comment by id
    """
    return await CommentService.update_comment(db, comment_id, comment.dict(), partial=True)













