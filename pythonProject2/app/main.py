from app.Classes.Request import Request
from app.Classes.Shop import Shop
from app.Classes.Store import Store
from app.Exception import NotEnoughProduct, NotName, NotEnoughСapacity, NotEnoughSpace

shop = Shop(items={})
shop.items = {"печеньки": 1, "торты": 2, "кексы": 1, "булочки": 1, "пироженные": 1}

store = Store(items={})
store.items = {"печеньки": 20, "булочки": 75, "мороженное": 4}


def main():
    """
    Функция main, которая обрабатывает ввод пользователя, выполните перемещение между складом и магазином если это возможно
    """
    while True:
        user_text = str(input(f'\nВведите запрос в формате "Доставить 3 печеньки из склад в магазин"\n'
                              f'Для выхода введите "stop"\n'))

        if user_text.lower() in ["stop", "стоп"]:
            break

        request = Request(user_text).to_dict()
        map_name = Request.map_name()
        if not map_name[request['from']]:
            break
        if map_name[request['from']] == 'store':
            try:
                store.remove(request["name"], request["count"])
            except NotName as error:
                print(error.message)
                continue
            except NotEnoughProduct as error:
                print(error.message)
                continue
            print(f"Нужное количество есть на складе\n",
                  f"Курьер забрал {request['count']} {request['name']} со {request['from']}\n",
                  f"Курьер везет {request['count']} {request['name']} со {request['from']} в {request['to']}")
            try:
                shop.add(request['name'], request["count"])
            except NotEnoughСapacity as error:
                print(error.message)
                store.add(request["name"], request["count"])
                continue
            except NotEnoughSpace as error:
                print(error.message)
                store.add(request["name"], request["count"])
                continue
            print(f"Курьер доставил {request['count']} {request['name']} в {request['to']}\n",
                  f"На складе хранится: {store.get_items()}\n",
                  f" В магазин хранится: {shop.get_items()}")

        elif map_name[request['from']] == 'shop':

            try:
                shop.remove(request["name"], request["count"])
            except NotName as error:
                print(error.message)
                continue
            except NotEnoughProduct as error:
                print(error.message)
                continue

            print("Нужное количество есть в магазине\n",
                  f"Курьер забрал {request['count']} {request['name']} со {request['from']}\n",
                  f"Курьер везет {request['count']} {request['name']} со {request['from']} в {request['to']}")

            try:
                store.add(request['name'], request["count"])
            except NotEnoughСapacity as error:
                print(error.message)
                shop.add(request["name"], request["count"])
                continue
            print(f"Курьер доставил {request['count']} {request['name']} в {request['to']}\n",
                  f"На складе хранится: {store.get_items()}\n",
                  f"В магазин хранится: {shop.get_items()}")


print(main())
