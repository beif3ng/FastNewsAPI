import uuid

from fastapi_users import schemas
from pydantic import BaseModel, EmailStr


class UserRead(schemas.BaseUser[uuid.UUID]):
    full_name: str


class UserCreate(schemas.BaseUserCreate):
    full_name: str


class UserUpdate(schemas.BaseUserUpdate):
    full_name: str | None = None


class VerificationRequestSchema(BaseModel):

    email: EmailStr

class VerificationSchema(BaseModel):

    email: EmailStr
    code: str