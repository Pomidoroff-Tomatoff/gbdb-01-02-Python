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
        1. Клетка не может состоять из ячеек -- нет такого в биологии. Это ошибка какая-то... 
           Но зато из клеток состоит клеточная ткань  -- целлюлоза, клетчатка.
           Следовательно,
              > объект верхнего уровня для нашей задачи -- 
                это ТКАНЬ из клеток: класс Cellulose
              > составным элементом этого класса будет клетка --
                это атрибут экземпляра класса cells.  
        2. Вынос проверок аргумента в родительский класс, см. 3_cell_experiment.py
     '''
print(homework_type)


class Cellulose:
    '''
        Клетки объединённые в единую ткань -- Целлюлозу
    '''
    def __init__(self, cells: int = None):
        if cells is None or cells <= 0:
            raise ValueError("Ошибка инициализации: количество клеток не должно быть = {}".format(quantity))
        if not isinstance(cells, int):
            raise ValueError("Ошибка инициализации: количество клеток задаётся только целым числом (int), а не типом {}".format(type(quantity)))

        self.__cells = cells  # количество клеток (приватное)

    def get_cells(self):      # интерфейс к приватному атрибуту на чтение вне класса (для второго операнда)
        return self.__cells

    def __type_verify(self, other):  # проверка типа операнда (аргумента)
        if not isinstance(other, self.__class__):
            raise TypeError("Ошибка: типы операндов должны соответствовать {}".format(self.__class__))

    def __call__(self):
        return self.get_cells()

    def __str__(self):
        return "Количество клеток (ячеек) в ткани = {}".format(self.get_cells())

    def __add__(self, other):
        self.__type_verify(other)  # проверка типа аргумента
        sum_quantity = self.get_cells() + other.get_cells()
        sum_obj = self.__class__(sum_quantity)
        return sum_obj

    def __iadd__(self, other):
        self.__type_verify(other)  # проверка типа аргумента
        self.__cells += other.get_cells()
        return self

    def __sub__(self, other):
        self.__type_verify(other)  # проверка типа аргумента
        sub_quantity = self.get_cells() - other.get_cells()
        if sub_quantity <= 0:
            raise ValueError("Ошибка вычитания: вычитающий объект больше вычитаемого")
        sub_obj = self.__class__(sub_quantity)
        return sub_obj

    def __mul__(self, other):
        self.__type_verify(other)  # проверка типа аргумента

        multiply_quantity = self.get_cells() * other.get_cells()
        multiply_obj = self.__class__(multiply_quantity)
        return multiply_obj

    def __truediv__(self, other):
        self.__type_verify(other)  # проверка типа аргумента
        if other.get_cells() == 0:
            raise ValueError("Ошибка деления: делить на ноль нельзя.")

        division = self.get_cells() // other.get_cells()
        if division <= 0:
            raise ValueError("Ошибка деления: результатом целочисленного деления не может быть ноль (0)")
        return self.__class__(division)

    def __floordiv__(self, other):
        division_obj = self.__truediv__(other)
        return division_obj

    def make_order(self, row_size: int = None):
        ''' Метод возвращает ряды клеток (ячеек) '''
        if not isinstance(row_size, int) or row_size is None or row_size <= 0:
            raise ValueError(f"Ряды ячеек: Недопустимое значение ряда {row_size = }")

        full_rows = self.get_cells() // row_size
        partial_size = self.get_cells() - full_rows * row_size
        rows = ("*" * row_size + "\n") * full_rows + "*" * partial_size + "\n"
        return rows

    pass  # Cellulose


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
