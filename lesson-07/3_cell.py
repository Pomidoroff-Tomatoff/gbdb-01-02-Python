# GeekBrains > Python basics: Oleg Gladkiy (https://geekbrains.ru/users/3837199)
homework_type = "Lesson-7. 3-Cellulose: Cell in biology"
'''
# 3. Реализовать программу работы с органическими клетками, состоящими из ячеек. 
     Необходимо создать класс Клетка. 
     В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). 
     В классе должны быть реализованы методы перегрузки арифметических операторов: 
        -- сложение (__add__()), 
        -- вычитание (__sub__()), 
        -- умножение (__mul__()), 
        -- деление (__truediv__()). 
     Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, 
     умножение и целочисленное (с округлением до целого) деление клеток, соответственно.
     
#    Сложение. 
        Объединение двух клеток. 
        При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
#    Вычитание. 
        Участвуют две клетки. 
        Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
#    Умножение. 
        Создается общая клетка из двух. 
        Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
#    Деление. 
        Создается общая клетка из двух. 
        Число ячеек общей клетки определяется как цело-численное деление количества ячеек этих двух клеток.

#    В классе необходимо реализовать метод make_order(), 
     -- принимающий экземпляр класса и количество ячеек в ряду. 
     -- Данный метод позволяет организовать ячейки по рядам.
#    -- Метод должен возвращать строку вида *****\n*****\n*****..., 
        где количество ячеек между \n равно переданному аргументу. 
        Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
#    Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n**.
#    Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n*****.
#    Подсказка: 
        подробный список операторов для перегрузки доступен по ссылке (https://pythonworld.ru/osnovy/peregruzka-operatorov.html).

     ИСПРАВЛЕНИЯ:
        1. "Клетка состоит из ячеек" реализовано для клеточной ткани (клетчатки, целюлозы), состоящей из клеток.
        2. ... 
     '''
print(homework_type)

import time
import abc

class Fiber(abc.ABC):
    '''
        Волокно:
        -- основная проверка ошибок
        -- базовые методы
        -- предполагалось, что идея разбить класс на шаблон и рабочий -- хорошая...
    '''
    def __init__(self, quantity: int = None):
        if quantity is None or quantity <= 0:
            raise ValueError("Ошибка инициализации: количество клеток не должно быть = {}".format(quantity))
        if not isinstance(quantity, int):
            raise ValueError("Ошибка инициализации: количество клеток задаётся только целым числом, а не типом {}".format(type(quantity)))
        self.__quantity = quantity

    def get_quantity(self):  # интерфейс к атрибуту
        return self.__quantity

    def set_quantity(self, quantity: int):
        if not isinstance(quantity, int):
            raise ValueError("Ошибка параметра: количество клеток задаётся только целым числом, а не типом {}".format(type(quantity)))
        self.__quantity = quantity

    pass  # Fiber


class Cellulose(Fiber):
    '''
        Целлюлоза
    '''
    def __init__(self, quantity: int):
        super().__init__(quantity=quantity)

    def __call__(self):
        return self.get_quantity()

    def __str__(self):
        return "Количество клеток (ячеек) в ткани = {}".format(self.get_quantity())

    def __add__(self, other):
        sum_quantity = self.__class__(self.get_quantity() + other.get_quantity())
        return sum_quantity

    def __iadd__(self, other):
        self.set_quantity(self.get_quantity() + other.get_quantity())
        return self

    def __sub__(self, other):
        sub_quantity = self.get_quantity() - other.get_quantity()
        if sub_quantity <= 0:
            raise ValueError("Ошибка вычитания: вычитающий объект больше вычитаемого")
        return self.__class__(sub_quantity)

    def __mul__(self, other):
        if not isinstance(other, self.__class__):
            raise ValueError("Ошибка: типы должны соответствовать {}".format(self.__class__))
        multiply = self.get_quantity() * other.get_quantity()
        return self.__class__(multiply)

    def __truediv__(self, other):
        if not isinstance(other, self.__class__):
            raise ValueError("Ошибка: типы должны соответствовать {}".format(self.__class__))
        if other.get_quantity() == 0:
            raise ValueError("Ошибка деления: делить на ноль нельзя.")
        division = self.get_quantity() // other.get_quantity()
        if division <= 0:
            raise ValueError("Ошибка деления: результатом целочисленного деления не может быть ноль (0)")
        return self.__class__(division)

    def __floordiv__(self, other):
        return self.__truediv__(other)

    def make_order(self, row_size: int = None):
        ''' Метод возвращает ряды клеток (ячеек) '''
        if not isinstance(row_size, int) or row_size is None or row_size <= 0:
            raise ValueError(f"Ряды ячеек: Недопустимое значение ряда {row_size = }")
        full_rows = self.get_quantity() // row_size
        partial_size = self.get_quantity() - full_rows * row_size
        rows = ("*" * row_size + "\n") * full_rows + "*" * partial_size + "\n"
        return rows

    pass  # Cellulose(Fiber)


# Поехали!

fiber_01 = Cellulose(1)
fiber_02 = Cellulose(3)
print(f"Вычитание .. {(Cellulose(2) - Cellulose(1))()  = }")
fiber_01 += fiber_02
print(f"Сложение с добавкой fiber_01 += fiber_02 .... = {fiber_01()}")
print(f"Умножение .. {(Cellulose(2) * Cellulose(3))()  = }")
print(f"Деление .... {(Cellulose(7) / Cellulose(2))()  = }")
print(f"Деление .... {(Cellulose(3) // Cellulose(2))() = }")
print(f"РЯДЫ:\n{(rows:=Cellulose(22).make_order(6)) = }\nИЛИ:\n{rows}")


print("End")
