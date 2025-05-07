from typing import Generic, List

from generics import TBaseEntity


class DbList(List[TBaseEntity], Generic[TBaseEntity]):
    def __init__(self, *args: TBaseEntity):
        super().__init__(*args)
        for item in args:
            self.append(item)

    def append(self, item: TBaseEntity) -> None:
        super().append(item)

    def find_by_id(self, id: int) -> TBaseEntity | None:
        for item in self:
            if item.id == id:
                return item
        return None
