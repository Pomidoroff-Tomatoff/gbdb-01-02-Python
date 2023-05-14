# GeekBrains > Python basics: Oleg Gladkiy (https://geekbrains.ru/users/3837199)
homework_type = "Lesson-7. 2-Dress"
'''
# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. 
     Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название. 
     К типам одежды в этом проекте относятся пальто и костюм. 
     У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). 
     Это могут быть обычные числа: V и H, соответственно.
      
     Для определения расхода ткани по каждому типу одежды использовать формулы: 
     -- для пальто (V/6.5 + 0.5), 
     -- для костюма (2*H + 0.3). 
     Проверить работу этих методов на реальных данных.
     Реализовать общий подсчет расхода ткани.
      
     Проверить на практике полученные на этом уроке знания: 
     -- реализовать абстрактные классы для основных классов проекта, 
     -- проверить на практике работу декоратора @property. 
     
     НЕУДАЧИ:
        1. Не удаётся организовать абстрактный метод приватным или защищённым...
        2. Метод-свойство (@property) не наследуется... 
     '''
print(homework_type)

import time
import abc
# from accessify import protected


class Dress(abc.ABC):
    # Общий класс для одежды
    def __init__(self, dress_param: int = None):
        # общая реакция на ошибку параметра
        self.err_dress_param = "DRESS: недопустимый размер или рост = {}."
        if dress_param is None: raise ValueError(self.err_dress_param.format(dress_param))
        elif dress_param <= 0:  raise ValueError(self.err_dress_param.format(dress_param))

        self.__rate = 0
        self.size = dress_param

    @abc.abstractmethod
    def fabric_consumption(self):
        ''' расход ткани '''
        pass

    pass  # Dress


class OverCoat(Dress):
    # Пальто
    def __init__(self, v: int = None):
        super().__init__(dress_param=v)
        if v < 18 or v > 78: raise ValueError(f"OverCoat. {v=}. Допустимый размер пальто: от 18 до 78")
        self.v = v
        self.__rate = self.fabric_consumption()

    def fabric_consumption(self):
        super().fabric_consumption()
        rate = self.v / 6.5 + 0.5
        return rate

    @property
    def get_rate(self):
        # интерфейс
        return self.__rate

    pass  # OverCoat(Dress) -- пальто


class Costume(Dress):
    # Костюм 
    def __init__(self, h: int = None):
        super().__init__(dress_param=h)
        if h < 38 or h > 70: raise ValueError(f"{h=}! Допустимый размер костюма: от 38 до 70")
        self.h = h
        self.__rate = self.fabric_consumption()

    def fabric_consumption(self):
        super().fabric_consumption()
        rate = self.h * 2 + 0.3
        return rate

    @property
    def get_rate(self):
        # интерфейс
        return self.__rate

    pass  # Costume(Dress) -- костюм


# Поехали: пальто...

print("РАСЧЁТЫ ДЛЯ ПАЛЬТО:")
print(f"Пальто размер {(v:=18)}, расход ткани = {OverCoat(v).get_rate: 8.3f}")
print(f"Пальто размер {(v:=56)}, расход ткани = {OverCoat(v).get_rate: 8.3f}")
print(f"Пальто размер {(v:=78)}, расход ткани = {OverCoat(v).get_rate: 8.3f}")
# OverCoat(0).get_rate         # проверка контроля ошибки аргумента

# а теперь костюмы...

print("РАСЧЁТЫ ДЛЯ КОСТЮМА:")
c1, c2, c3 = Costume(38), Costume(56), Costume(70)
print(f"Костюм размер {c1.size}, расход ткани = {c1.get_rate: 8.3f}")
print(f"Костюм размер {c2.size}, расход ткани = {c2.get_rate: 8.3f}")
print(f"Костюм размер {c3.size}, расход ткани = {c3.get_rate: 8.3f}")
# Costume(None).get_rate       # проверка контроля ошибки аргумента

print("End")
