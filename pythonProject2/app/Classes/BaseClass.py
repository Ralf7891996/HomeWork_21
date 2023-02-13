from app.Classes.Storage import Storage
from app.Exception import NotEnoughProduct, NotName, NotEnoughСapacity


class BaseClass(Storage):
    def __init__(self, items: dict, capacity: int):
        self._capacity = capacity
        self._items = items

    @property
    def items(self):
        return self._items

    @property
    def capacity(self):
        return self._capacity

    @items.setter
    def items(self, new_data):
        self._items = new_data

    def add(self, name: str, count: int):
        if self.get_free_space() < count:
            raise NotEnoughСapacity
        if name in self._items.keys():
            self._items[name] += count
        else:
            self._items[name] = count

    def remove(self, name, count):
        if name not in self._items.keys():
            raise NotName
        if self._items[name] < count:
            raise NotEnoughProduct
        else:
            self._items[name] -= count

        if self._items[name] == 0:
            self._items.pop(name)

    def get_free_space(self):
        return self._capacity - sum(self._items.values())

    def get_items(self):
        return self._items

    def get_unique_items_count(self):
        return len(self._items)

