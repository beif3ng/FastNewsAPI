# FastNewsAPI

An asynchronous news platform REST API built with FastAPI. Supports user registration and JWT authentication, categorized news articles with image attachments, and threaded comments. Backed by PostgreSQL via async SQLAlchemy and containerized with Docker.

## Features

- User registration and JWT authentication via `fastapi-users`
- Full CRUD for news categories, articles, and comments
- Image arrays per article (stored as PostgreSQL `ARRAY`)
- Background tasks with Celery + Redis
- Database migrations with Alembic
- Fully async: `asyncpg` + SQLAlchemy 2.0 mapped columns
- Dockerized stack (PostgreSQL + Redis + FastAPI)

## Tech Stack

| Layer | Technology |
|---|---|
| Web framework | FastAPI 0.115 |
| Auth | fastapi-users 14 (JWT) |
| Database | PostgreSQL + asyncpg |
| ORM | SQLAlchemy 2.0 (async) |
| Migrations | Alembic |
| Task queue | Celery 5.4 + Redis |
| Deployment | Docker Compose |

## Data Model

```
User
 └──< Comment

Category
 └──< News >──< Comment
```

| Model | Key Fields |
|---|---|
| `User` | `id` (UUID), `email`, `hashed_password` |
| `Category` | `name`, `created` |
| `News` | `title`, `content`, `images[]`, `category_id`, `created`, `updated` |
| `Comment` | `text`, `news_id`, `user_id`, `created`, `updated` |

## Project Structure

```
FastNewsAPI/
├── main.py                     # FastAPI app, router registration
├── src/
│   ├── database.py             # Async engine and session factory
│   ├── environs.py             # Settings from .env
│   ├── celery.py               # Celery app config
│   ├── manager.py              # User manager (fastapi-users)
│   └── news/
│       ├── models.py           # Category, News, Comment ORM models
│       ├── routers/            # categories.py, news.py, comments.py
│       ├── schemas/            # Pydantic read/write schemas
│       └── services/           # Business logic layer
├── alembic/                    # Migration scripts
├── docker-compose.yml
├── .env.example
└── requirements.txt
```

## Getting Started

### Local Setup

```bash
git clone https://github.com/beif3ng/FastNewsAPI.git
cd FastNewsAPI
cp .env.example .env  # fill in your values
pip install -r requirements.txt
alembic upgrade head
uvicorn main:app --reload
```

### Docker

```bash
cp .env.example .env.docker
docker compose up --build
```

### Start Celery Worker

```bash
celery -A src.celery:celery_app worker -l info
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/auth/register` | Register a new user |
| POST | `/auth/jwt/login` | Log in and receive JWT |
| GET / POST | `/categories/` | List or create categories |
| GET / POST | `/news/` | List or create news articles |
| GET | `/news/{id}` | Get article with comments |
| GET / POST | `/comments/` | List or create comments |

Interactive docs available at `/docs`.

## Environment Variables

| Variable | Description |
|---|---|
| `DB_HOST` | PostgreSQL host |
| `DB_PORT` | PostgreSQL port |
| `DB_NAME` | Database name |
| `DB_USER` | Database user |
| `DB_PASSWORD` | Database password |
| `USER_MANAGER_SECRET` | Secret for user manager token |
| `JWT_SECRET` | JWT signing secret |
