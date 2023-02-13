from app.Classes.BaseClass import BaseClass


class Store(BaseClass):
    def __init__(self, items: dict, capacity: int = 100):
        super().__init__(items, capacity)


