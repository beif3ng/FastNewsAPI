"""
Module reads environ variables
"""

import os

from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv("DB_NAME", "postgres")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")

JWT_SECRET = os.getenv("JWT_SECRET", "SECRET")
USER_MANAGER_SECRET = os.getenv("USER_MANAGER_SECRET", "SECRET")

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
BASE_URL = os.getenv("BASE_URL", "http://localhost:8000")

SMTP_PORT = os.getenv("SMTP_PORT", SMTP_PORT)
SMTP_HOST = os.getenv("SMTP_HOST", "smtp.gmail.com")
SMTP_USER = os.getenv("SMTP_USER", "user@example.com")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "password")

MEDIA_ROOT = "media/"

__all__ = [
    "DB_NAME",
    "DB_USER",
    "DB_PASSWORD",
    "DB_HOST",
    "DB_PORT",

    "BASE_URL",
    "REDIS_URL",

    "SMTP_PORT",
    "SMTP_HOST",
    "SMTP_USER",
    "SMTP_PASSWORD",
]