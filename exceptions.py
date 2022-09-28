class BaseError(Exception):
    message = "Какая-то ошибка"


class NotEnoughSpace(BaseError):
    message = "Недостаточно места в магазине"


class NotEnoughProduct(BaseError):
    message = "Недостаточно товара на складе"


class TooManyDifferentProducts(BaseError):
    message = "Слишком много разных товаров"


class InvalidRequest(BaseError):
    message = "Неправильный запрос. Попробуй снова"


class InvalidName(BaseError):
    message = "Неправильное название точки отгрузки или получения"
