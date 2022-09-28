from exceptions import TooManyDifferentProducts
from packege.storage import Storage


class Shop(Storage):
    def __init__(self, items: dict, capacity: int = 20):
        super().__init__(items, capacity)

    def add(self, name: str, quantity: int):
        if self.get_unique_items_count() >= 5:
            raise TooManyDifferentProducts

        super().add(name, quantity)
