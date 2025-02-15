"""
Routers for news app
"""
from typing import Sequence

from fastapi import APIRouter, HTTPException
from sqlalchemy import select

from .models import News
from .schemas import NewsReadSchema, NewsCreateSchema

from src.database import session as async_session

news_router = APIRouter(
    prefix="/news",
    tags=["News"]
)


@news_router.get("", response_model=Sequence[NewsReadSchema])
async def get_news(offset: int = 0, limit: int = 10) -> Sequence[News]:
    """
    Get all news
    """
    async with async_session() as session:
        query = select(News).offset(offset).limit(limit)
        result = await session.execute(query)
        news = result.scalars().all()
        return news


@news_router.get("/{news_id}", response_model=NewsReadSchema)
async def get_news(news_id: int) -> News:
    """
    Get news by id
    """
    async with async_session() as session:
        query = select(News).where(News.id == news_id)
        result = await session.execute(query)
        news = result.scalar_one_or_none()
        if news is None:
            raise HTTPException(status_code=404, detail="News not found")
        return news


@news_router.post("", response_model=NewsReadSchema)
async def create_news(news: NewsCreateSchema) -> News:
    """
    Create news
    """
    async with async_session() as session:
        new_news = News(**news.dict())
        session.add(new_news)
        await session.commit()
        await session.refresh(new_news)
        return new_news


@news_router.delete("/{news_id}")
async def delete_news(news_id: int):
    """
    Delete news by id
    """
    async with async_session() as session:
        query = select(News).where(News.id == news_id)
        result = await session.execute(query)
        news = result.scalar_one_or_none()
        if news is None:
            raise HTTPException(status_code=404, detail="News not found")
        await session.delete(news)
        await session.commit()


@news_router.put("/{news_id}", response_model=NewsReadSchema)
async def update_news(news_id: int, news: NewsCreateSchema) -> News:
    """
    Update news by id
    """
    async with async_session() as session:
        query = select(News).where(News.id == news_id)
        result = await session.execute(query)
        old_news = result.scalar_one_or_none()
        if old_news is None:
            raise HTTPException(status_code=404, detail="News not found")

        for field, value in news.dict().items():
            setattr(old_news, field, value)

        await session.commit()
        await session.refresh(old_news)
        return old_news


@news_router.patch("/{news_id}", response_model=NewsReadSchema)
async def partial_update_news(news_id: int, news: NewsCreateSchema) -> News:
    """
    Update news by id
    """
    async with async_session() as session:
        query = select(News).where(News.id == news_id)
        result = await session.execute(query)
        old_news = result.scalar_one_or_none()
        if old_news is None:
            raise HTTPException(status_code=404, detail="News not found")

        for field, value in news.dict().items():
            if value:
                setattr(old_news, field, value)

        await session.commit()
        await session.refresh(old_news)
        return old_news
