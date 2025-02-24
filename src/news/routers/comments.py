"""
Comments router
"""

from typing import Sequence, Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, Form, File, UploadFile, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_users.authentication import AuthenticationBackend

from src.database import get_db
from src.users.auth import auth_backend
from src.users.models import User
from src.users.routers import fastapi_users

from ..services import CommentService
from ..schemas import CommentReadSchema, CommentCreateSchema, CommentUpdateSchema
from ..models import Comment


router = APIRouter(
    prefix="/comments",
    tags=["Comment"]
)

current_user = fastapi_users.current_user()
current_active_user = fastapi_users.current_user(active=True)


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


@router.post("", response_model=CommentReadSchema)
async def create_comment(
    comment: CommentCreateSchema, 
    db: AsyncSession = Depends(get_db),
    user: User = Depends(current_active_user)
) -> Comment:
    """
    Create comment. Only for authorized users.
    """
    comment_data = comment.dict()
    comment_data["user_id"] = user.id
    return await CommentService.create_comment(db, comment_data)


@router.put("/{comment_id}", response_model=CommentReadSchema)
async def update_comment(
    comment_id: int, 
    comment: CommentUpdateSchema, 
    db: AsyncSession = Depends(get_db),
    user: User = Depends(current_active_user)
) -> Comment:
    """
    Update comment by id. Only for comment owners.
    """
    existing_comment = await CommentService.get_comment(db, comment_id)
    if existing_comment.user_id != user.id:
        raise HTTPException(status_code=403, detail="Not authorized to modify this comment")
    return await CommentService.update_comment(db, comment_id, comment.dict())


@router.patch("/{comment_id}", response_model=CommentReadSchema)
async def partial_update_comment(
    comment_id: int, 
    comment: CommentUpdateSchema, 
    db: AsyncSession = Depends(get_db),
    user: User = Depends(current_active_user)
) -> Comment:
    """
    Partial update comment by id. Only for comment owners.
    """
    existing_comment = await CommentService.get_comment(db, comment_id)
    if existing_comment.user_id != user.id:
        raise HTTPException(status_code=403, detail="Not authorized to modify this comment")
    
    update_data = comment.dict(exclude_unset=True)  # Only include set values
    return await CommentService.update_comment(db, comment_id, update_data, partial=True)


@router.delete("/{comment_id}", status_code=204)
async def delete_comment(
    comment_id: int, 
    db: AsyncSession = Depends(get_db),
    user: User = Depends(current_active_user)
) -> None:
    """
    Delete comment by id. Only for comment owners.
    """
    existing_comment = await CommentService.get_comment(db, comment_id)
    if existing_comment.user_id != user.id:
        raise HTTPException(status_code=403, detail="Not authorized to modify this comment")
    return await CommentService.delete_comment(db, comment_id)
