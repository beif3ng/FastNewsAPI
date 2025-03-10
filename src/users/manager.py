import uuid
from typing import Optional

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, UUIDIDMixin

from src.celery import print_user_data, send_verification_code
from src.redis import generate_verification_code, redis_client
from .models import User, get_user_db

SECRET = "SECRET"


class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")
        print_user_data.apply_async(args=[
            {
                "email": user.email,
                "full_name": user.full_name,
            }
        ])

        code = generate_verification_code()
        await redis_client.setex(
            name=user.email,
            time=600,
            value=code,
        )
        send_verification_code.apply_async(args=[user.email, code])

    async def on_after_forgot_password(
            self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(
            self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"Verification requested for user {user.id}. Verification token: {token}")


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)