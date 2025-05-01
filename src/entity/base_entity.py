from abc import ABC, abstractmethod

class BaseEntity(ABC):
    @property
    @abstractmethod
    def id(self) -> int:
        pass   
    
    @id.setter
    @abstractmethod
    def id(self, value: int| None) -> None:
        pass