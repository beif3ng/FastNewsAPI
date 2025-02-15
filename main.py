"""
Main program module
"""

from fastapi import FastAPI

from src.category import category_router
from src.news import news_router

app = FastAPI()

app.include_router(router=category_router)
app.include_router(router=news_router)

