from typing import AsyncGenerator
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
import os


class DatabaseSession:
    load_dotenv(dotenv_path="src/.env")
    login = os.getenv("DB_LOGIN")
    pwd = os.getenv("DB_PWD")

    def __init__(self) -> None:
        self.engine = create_async_engine(
            f"postgresql+asyncpg://{self.login}:{self.pwd}@localhost/hotel_booking_system",
            echo=True,
            future=True,
        )

        self.SessionLocal = sessionmaker(
            self.engine,
            class_=AsyncSession,
            expire_on_commit=False,
            autocommit=False,
            autoflush=False,
        )

    async def get_db(self) -> AsyncGenerator:
        async with self.SessionLocal() as session:
            try:
                yield session
            except Exception:
                await session.rollback()
                raise
            finally:
                await session.close()
