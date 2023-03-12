class NotEnoughSpace(BaseException):
    message = 'Невозможно доставить товар!\n'


class NotEnoughGoods(BaseException):
    message = 'Недостаточно товара!\n'


class NoGoodsInStorage(BaseException):
    message = 'Данного товара нет на складе!\n'


class MaxUniqueItemsInStorage(BaseException):
    message = 'Невозможно доставить товар!\n'


class BadRequest(BaseException):
    message = 'Неверный формат запроса!\n'