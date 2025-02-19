"""
Comments router
"""

from typing import Sequence, Annotated

from fastapi import APIRouter, Depends, Form, File, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_db

from ..services import NewsService
from ..schemas import NewsReadSchema, NewsReadDetailsSchema
from ..models import News