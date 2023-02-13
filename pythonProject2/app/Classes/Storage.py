from abc import ABC, abstractmethod


class Storage(ABC):
    """
    абстрактный класс Storage
    """

    @abstractmethod
    def add(self, name, count):
        raise NotImplementedError

    @abstractmethod
    def remove(self, name, count):
        raise NotImplementedError

    @abstractmethod
    def get_free_space(self):
        raise NotImplementedError

    @abstractmethod
    def get_items(self):
        raise NotImplementedError

    @abstractmethod
    def get_unique_items_count(self):
        raise NotImplementedError

