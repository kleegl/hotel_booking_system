from httpx import AsyncClient
import pytest
from random import random

from src.models import Hotel
from src.main import app


@pytest.fixture
def test_hotel_data():
    return {
        "name": f"name{random():.5f}",
        "location": f"location{random():.5f}",
        "base_price": 100.0,
        "capacity": 50,
    }


@pytest.mark.asyncio
async def test_create_hotel(test_hotel_data):
    async with AsyncClient(base_url="http://localhost:8000") as client:
        response = await client.post("/hotel/create", json=test_hotel_data)

        assert response.status_code == 200
        data = response.json()

        assert data["name"] == test_hotel_data["name"]
        assert data["location"] == test_hotel_data["location"]
        assert data["base_price"] == test_hotel_data["base_price"]
        assert data["capacity"] == test_hotel_data["capacity"]


@pytest.mark.asyncio
async def test_get_hotel(test_hotel_data):
    async with AsyncClient(base_url="http://localhost:8000") as client:
        create_response = await client.post("/hotel/create", json=test_hotel_data)
        assert create_response.status_code == 200
        data = create_response.json()

        get_response = await client.get(f"/hotel/{data["id"]}")
        assert get_response.status_code == 200
        assert get_response.json()["name"] == test_hotel_data["name"]
