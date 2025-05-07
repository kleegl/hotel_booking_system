from sqlalchemy import Column, Integer
from sqlalchemy.orm import as_declarative, declared_attr


@as_declarative()
class BaseEntity:
    id = Column(Integer, primary_key=True, index=True)

    @declared_attr
    def __tablename__(cls):
        return "".join([cls.__name__.lower(), "s"])
