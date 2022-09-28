from typing import Dict

from exceptions import InvalidRequest, BaseError
from packege.courier import Courier
from packege.request import Request
from packege.shop import Shop
from packege.store import Store

store = Store(items={
    "печеньки": 12,
    "собачки": 10,
    "коробки": 40,
    "иголки": 10,
    "зонты": 10
})

shop = Shop(items={
    "собачки": 2,
    "коробки": 5,
    "иголки": 1,
    "зонты": 1,
    "сумки": 2
})

storages = {
    "магазин": shop,
    "склад": store
}


def get_print(items: Dict[str, int]):
    for key in sorted(items):
        print(items[key], key)


def main():
    print("\nДобрый день!\n")

    while True:

        for storage_name in storages:
            print(f"В {storage_name} хранится:")
            get_print(storages[storage_name].get_items())
        user_input = input(
            'Введите запрос в формате "Доставить 3 печеньки из склад в магазин"\n'
            'Введите "стоп" , если хотите закончить:\n'
        )
        if user_input in ('стоп', 'stop'):
            break
        try:
            request = Request(request=user_input, storages=storages)
        except BaseError as error:
            print(error.message)
            continue

        courier = Courier(
            request=request,
            storages=storages,
        )
        try:
            courier.move()
        except BaseError as error:
            print(error.message)
            courier.cancel()


if __name__ == "__main__":
    main()
