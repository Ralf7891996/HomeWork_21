class NotName(Exception):
    message = 'Товар не обнаружен на складе'


class NotEnoughProduct(Exception):
    message = 'Не достаточно товара'


class NotEnoughСapacity(Exception):
    message = 'Не достаточно места, товар возвращен'


class NotEnoughSpace(Exception):
    message = 'Магазин наполнен, возврат на склад'