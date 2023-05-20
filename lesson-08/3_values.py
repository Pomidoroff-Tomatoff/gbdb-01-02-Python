# GeekBrains > Python basics: Oleg Gladkiy (https://geekbrains.ru/users/3837199)
homework_type = "Lesson-8. 2_values"
'''
  3. Создайте собственный класс-исключение, который должен проверять содержимое списка 
     на наличие только чисел. Проверить работу исключения на реальном примере. 
     Запрашивать у пользователя данные и заполнять список необходимо только числами. 
     Класс-исключение должен контролировать типы данных элементов списка.

     Примечание: 
        A. Длина списка не фиксирована. 
        Б. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, 
           введя, например, команду «stop». 
        B. При этом скрипт завершается, сформированный список с числами выводится на экран.

     Подсказка: 
        Для этого задания примем, что пользователь может вводить только числа и строки. 
        Во время ввода пользователем очередного элемента необходимо реализовать проверку типа элемента. 
        Вносить его в список, только если введено число. 
        
        Класс-исключение должен не позволить пользователю ввести текст (не число) 
        и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.
'''
print(homework_type)


class ApplicationDigitalError(Exception):
    ''' Прикладное ИСКЛЮЧЕНИЕ: введены буквы, а не цифры '''

    def __init__(self, message: str = ""):
        self.message = f"введены буквы, а не число / {message}"

    def __str__(self):
        return f"Ошибка: {self.message}"


class DigitalMagazine:
    ''' Магазин цисел '''

    values = []

    @classmethod
    def set_value(cls, value):
        if isinstance(value, list):
            cls.values.extend(value)
        else:
            cls.values.append(value)

    @classmethod
    def get_magazine(cls):
        return cls.values

    @staticmethod
    def get_value(prompt: str = ""):
        if (string := input(prompt)) and not string.isspace() and not (string.upper() == "STOP" or string.upper() == "ЫЕЩЗ"):
            try:
                return float(string)
            except ValueError as errmsg:
                raise ApplicationDigitalError(errmsg) from None

    def runner(self):
        print("МАГАЗИН ЧИСЕЛ: введите числа для помещения в список магазина (\"stop\" или просто Enter для завершения)")
        while True:
            try:
                if (value := self.get_value("  введите число: ")) is None: break

            except ApplicationDigitalError as err:
                print(err)
            except Exception as err:
                print(f"Обратитесь к администратору. Ошибка: {err}")
            else:
                self.set_value(value)

        print(f"СПИСОК ЧИСЕЛ: {self.get_magazine()}")

    def __call__(self, *args, **kwargs):
        self.runner()


# Поехали
if __name__ == "__main__":
    DigitalMagazine()()
    print("End")
