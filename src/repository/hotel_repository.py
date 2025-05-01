

from abc import ABC

from entity.hotel import Hotel
from repository.base_repository import IBaseRepository
from schemas.hotel_schema import HotelCreateSchema, HotelUpdateSchema


class IHotelRepository(IBaseRepository[Hotel, HotelCreateSchema, HotelUpdateSchema], ABC):
    pass


class HotelRepositroy(IHotelRepository, IBaseRepository[Hotel, HotelCreateSchema, HotelUpdateSchema]):
    def create(self, item: HotelCreateSchema) -> None:
        return super().create(item)
    
    
    def update(self, item: HotelUpdateSchema) -> None:
        return super().update(item)
    
    
    def delete(self, id: int) -> None:
        return super().delete(id)
    
    
    def get(self, id: int) -> Hotel | None:
        return super().get(id)
    
    
    def _map_to_entity(self, hotel: HotelCreateSchema) -> Hotel:
        return Hotel(id=hotel.id, name=hotel.name, location=hotel.location, base_price=hotel.base_price, capacity=hotel.capacity)


    def _update_entity(self, db_hotel: Hotel, hotel: HotelUpdateSchema) -> None:
        db_hotel.name = hotel.name
        db_hotel.location = hotel.location 
        db_hotel.base_price = hotel.base_price 
        db_hotel.capacity = hotel.capacity