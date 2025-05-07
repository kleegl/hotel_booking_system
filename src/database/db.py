from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
import os

login = os.getenv("DB_LOGIN")
pwd = os.getenv("DB_PWD")

engine = create_async_engine(
    f"postgresql+asyncpg://{login}:{pwd}@localhost/hotel_booking_system"
)

async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_db():
    db = async_session()
    try:
        yield db
    finally:
        db.close()
