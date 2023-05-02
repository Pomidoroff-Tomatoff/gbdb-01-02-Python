# GeekBrains > Python basics: Oleg Gladkiy (https://geekbrains.ru/users/3837199)
homework_type = "Lesson-7. 3-Cellulose: Cell in biology (experimentary)"
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
     ИСПРАВЛЕНИЯ:
        1. Клетка не может состоять из ячеек -- нет такого в биологии. 
           Но клеточная ткань может состоять из клеток. 
           Реализация класса: как клеточная ткань (клетчатка, целюлоза), 
           состоящая из клеток.
        2. эксперимент с родительским классом и "движком" из приватных методами в нём для следующего:
           > вынос проверок аргументов только в родительский класс
           > разрешение ограничения использования приватных методов рамками класса:
           > передача приватного метода от экз. родителя к экз. потомка:
             -- задействуем конструкторы экземпляров классов
             -- передаём адрес метода от родительского экземпляра к дочернему экз. классу
                при помощи не приватных переменных
             -- пере-присваиваем адреса приватныех родительскиех методов дочерним приватным атрибутам,
                которые теперь станут методами (если к ним так обращаться).  
             -- удаляем в экз. потомка неприватные переменные передачи адресов, чтобы не было возможности... 
     '''
print(homework_type)

import time
import abc

class Fiber(abc.ABC):
    '''
        Волокно (шаблон):
        -- проверка входящих данных
    '''
    def __init__(self, quantity: int = None):
        if quantity is None or quantity <= 0:
            raise ValueError("Ошибка инициализации: количество клеток не должно быть = {}".format(quantity))
        if not isinstance(quantity, int):
            raise TypeError("Ошибка инициализации: количество клеток задаётся только целым числом, а не типом {}".format(type(quantity)))

        self.__cells = quantity  # ГЛАВНЫЙ АТРИБУТ

        # передача наследнику адресов приватных методов неприватными атрибутами...
        self._function__set_cells_quantity = self.__set_cells_quantity

    def __set_cells_quantity(self, quantity: int = 0):  # интерфейс к атрибуту
        # self.__init__(quantity)
        if quantity is None or quantity <= 0:
            raise ValueError("Ошибка инициализации: количество клеток {} не должно быть больше нуля".format(quantity))
        if not isinstance(quantity, int):
            raise TypeError("Ошибка: количество клеток задаётся только целым числом, а не типом {}".format(type(quantity)))
        self.__cells = quantity
        return self.__cells

    def get_cells_quantity(self):  # интерфейс к атрибуту
        return self.__cells

    def len(self):                 # интерфейс, повтор для удобства
        return self.__cells

    def __type_matching_check(self, other):  # проверка типа другого операнда
        if not isinstance(other, self.__class__):
            raise TypeError("Ошибка: типы должны соответствовать {}".format(self.__class__))

    def __add__(self, other):
        self.__type_matching_check(other)

    def __iadd__(self, other):
        self.__type_matching_check(other)

    def __sub__(self, other):
        self.__type_matching_check(other)
        if self.get_cells_quantity() < other.get_cells_quantity():
            raise ValueError("Ошибка вычитания: вычитающий объект больше вычитаемого")

    def __mul__(self, other):
        self.__type_matching_check(other)

    def __truediv__(self, other):
        self.__type_matching_check(other)
        if other.get_cells_quantity() == 0:
            raise ValueError("Ошибка деления: делить на ноль нельзя.")

    def make_order(self, row_size: int = None):
        if not isinstance(row_size, int) or row_size is None or row_size <= 0:
            raise ValueError(f"Ряды ячеек: Недопустимое значение ряда {row_size = }")

    pass  # Fiber


class Cellulose(Fiber):
    '''
        Клетки, объединённые в единую ткань -- Целлюлозу
    '''
    def __init__(self, cells: int):
        super().__init__(quantity=cells)
        # Получаем приватные методы от родителя (и заметам следы):
        self.__set_cells_quantity = self._function__set_cells_quantity
        self._function__set_cells_quantity = None
        del self._function__set_cells_quantity

    def __call__(self):
        return self.get_cells_quantity()

    def __str__(self):
        return "Количество клеток (ячеек) в ткани = {}".format(self.get_cells_quantity())

    def __add__(self, other):
        super().__add__(other)
        return self.__class__(self.get_cells_quantity() + other.get_cells_quantity())

    def __iadd__(self, other):
        super().__iadd__(other)
        self.__set_cells_quantity(self.get_cells_quantity() + other.get_cells_quantity())
        return self

    def __sub__(self, other):
        super().__sub__(other)
        return self.__class__(self.get_cells_quantity() - other.get_cells_quantity())

    def __mul__(self, other):
        super().__mul__(other)
        return self.__class__(self.get_cells_quantity() * other.get_cells_quantity())

    def __truediv__(self, other):
        super().__truediv__(other)
        division = self.get_cells_quantity() // other.get_cells_quantity()
        if division <= 0:
            raise ValueError("Ошибка деления: результатом целочисленного деления не может быть ноль (0)")
        return self.__class__(division)

    def __floordiv__(self, other):
        return self.__truediv__(other)

    def make_order(self, row_size: int = None):
        ''' ряды клеток  '''
        super().make_order(row_size=row_size)  # проверка аргумента
        full_rows = self.get_cells_quantity() // row_size
        partial_size = self.get_cells_quantity() - full_rows * row_size
        rows = ("*" * row_size + "\n") * full_rows + "*" * partial_size + "\n"
        return rows

    pass  # Cellulose(Fiber)


# Поехали!

fiber_01 = Cellulose(1)
print(f"{fiber_01() = }")
print(fiber_01)
print(f"Сложение ... {(Cellulose(2) + Cellulose(1))()  = }")
print(f"Вычитание .. {(Cellulose(2) - Cellulose(1))()  = }")
fiber_01 += Cellulose(3)
print(f"Сложение с добавкой fiber_01 += Cellulose(3)  = {fiber_01()}")
print(f"Умножение .. {(Cellulose(2) * Cellulose(3))()  = }")
print(f"Деление .... {(Cellulose(7) / Cellulose(2))()  = }")
print(f"Деление .... {(Cellulose(3) // Cellulose(2))() = }")
print(f"РЯДЫ:\n{(rows:=Cellulose(22).make_order(6)) = }\nИЛИ:\n{rows}")



print("End")
