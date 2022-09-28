from typing import Dict

from exceptions import NotEnoughSpace, NotEnoughProduct
from packege.abs_storage import AbstractStorage


class Storage(AbstractStorage):
    def __init__(self, items: Dict[str, int], capacity: int):

        self.__items = items
        self.__capacity = capacity

    def add(self, name: str, quantity: int):
        if self.get_free_space() < quantity:
            raise NotEnoughSpace
        if name in self.__items:
            self.__items[name] += quantity
        else:
            self.__items[name] = quantity

    def remove(self, name: str, quantity: int):
        if name not in self.__items or self.__items[name] < quantity:
            raise NotEnoughProduct

        self.__items[name] -= quantity
        if self.__items[name] == 0:
            self.__items.pop(name)

    def get_free_space(self):
        current_space = 0
        for value in self.__items.values():
            current_space += value
        return self.__capacity - current_space

    def get_items(self):
        return self.__items

    def get_unique_items_count(self):
        return len(self.__items)
