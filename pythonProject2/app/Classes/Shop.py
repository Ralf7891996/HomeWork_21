from pythonProject2.app.Classes.BaseClass import BaseClass
from pythonProject2.app.Exception import NotEnoughСapacity, NotEnoughSpace


class Shop(BaseClass):
    def __init__(self, items: dict, capacity: int = 20):
        super().__init__(items, capacity)

    def add(self, name, count):
        if self.get_free_space() < count:
            raise NotEnoughСapacity
        if name in self._items.keys():
            self._items[name] += count
        else:
            if self.get_unique_items_count() >= 5:
                raise NotEnoughSpace
            self._items[name] = count





