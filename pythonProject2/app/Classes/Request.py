
class Request:

    """
    Класс принимает запрос в текстовом виде и возвращает словарь
    """
    def __init__(self, user_text: str):
        self.user_text = user_text

    def to_dict(self):
        self.user_text = self.user_text.lower()
        user_text_list = self.user_text.split(' ')
        try:
            count = user_text_list[(user_text_list.index('доставить') + 1)]
            name = user_text_list[(user_text_list.index('доставить') + 2)]
            from_1 = user_text_list[(user_text_list.index('из') + 1)]
            to = user_text_list[(user_text_list.index('в') + 1)]
        except ValueError:
             print("Не верный формат запроса")

        return {"from": from_1,
                "to": to,
                "name": name,
                "count": int(count)}

    @staticmethod
    def map_name():
        return {"склад": "store",
                "магазин": "shop"}

