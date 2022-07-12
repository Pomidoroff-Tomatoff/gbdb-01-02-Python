# GeekBrains > Python basics: Oleg Gladkiy (https://geekbrains.ru/users/3837199)
homework_type = "Lesson-6. 4-Car"
# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
#    speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
#    которые должны сообщать, что машина поехала, остановилась, повернула (куда).
#    Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
#    Добавьте в базовый класс метод show_speed, который должен показывать текущую
#    скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
#    При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение
#    о превышении скорости.
#    Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ
#    к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
print(homework_type)


class Car:
    __cars_total = 0
    __turns_dict = {'straight': (1, 'прямо'),
                    'left': (2, 'налево'),
                    'right': (3, 'направо')}  # 3-и поворота
    __directs_dict = {'forward': (1, 'вперёд'),
                      'back': (-1, 'назад')}  # 2-а направления
    __car_type = {}  # наверное, тип машин также следует держать в словаре...

    def __init__(self, name, color, is_police=False, type_car=None):
        Car.__cars_total += 1  # порядковый номер созданного экземпляра
        self.__car_number = Car.__cars_total  # всего создано экземпляров

        self.__name = name
        self.__type_car = type_car
        self.__color = color
        self.__is_police = is_police
        self.__speed = 0
        self.__direction, self.__direction_name = Car.__directs_dict['forward']
        self.__turn, self.__turn_name = Car.__turns_dict['straight']
        # self.__car_speed_max -- не передать приватную переменную для дочерних классов
        self.info_car = ""
        print(f"\nСоздана машина по имени «{self.__name}», "
              f"цвета «{self.__color}», типа \"{self.__type_car}\", "
              f"номер {self.__car_number}.")
        if self.__is_police:
            print("Автомобиль для полиции")

    def go(self, speed):
        if speed == 0:
            self.stop()
        elif speed > 0:
            self.__speed = speed
            print(f"-- машина «{self.__name}/{self.__car_number}» поехала со скоростью {self.__speed} км/ч "
                  f"{self.__direction_name} и {self.__turn_name}.")
        else:
            print(f"-- Ошибка! Неудачная попытка здать скорость машины «{self.__name}/{self.__car_number}», "
                  f"равной {speed} км/ч.")

    def stop(self):
        if self.__speed > 0:
            self.__speed = 0
            print(f"-- машина «{self.__name}/{self.__car_number}» остановилась")
        else:
            self.__speed = 0
            print(f"-- машина «{self.__name}/{self.__car_number}» уже была остановлена")

    def set_turn(self, turn='forward'):
        try:
            self.__turn, self.__turn_name = Car.__turns_dict[turn]
            print(f"-- машина «{self.__name}/{self.__car_number}», поворот руля: {self.__turn_name}.")
        except KeyError:
            print(f"ОШИБКА: Неверно задано направление движения")
        except:
            print(f"ОШИБКА: неизвестная ошибка программы")
        finally:
            return

    def set_direct(self, direction):
        pass

    def show_speed(self):
        print(f"Текущая скорость движения {self.__speed} км/ч.")

    def get_speed(self):
        return self.__speed  # необходима для доступа к атрибуту "скорость" из дочерних классов


class TownCar(Car):
    def __init__(self, name, color):
        super().__init__(name, color, is_police=False, type_car='TownCar')
        self.info = "Городской автомобиль"
        self.__car_speed_max = 60  # область видимости -- только это класс, но больше нам и не надо
        # __speed доступна только в классе-родителе, где она определена
        # чтобы получить к ней доуступ необходим нЕприватный метод класса их этого эже класса,
        # то есть в родетеле Car.

    def show_speed(self):
        if self.get_speed() > self.__car_speed_max:
            print(f"-- ВНИМАНИЕ! текущая скорость движения {self.get_speed()} км/ч "
                  f"превышает ограничение в {self.__car_speed_max} км/ч для данного типа!")
        else:
            print(f"Текущая скорость движения {self.get_speed()} км/ч.")


class WorkCar(Car):
    def __init__(self, name, color):
        super().__init__(name, color, is_police=False, type_car='WorkСar')
        self.info = "Грузовик"
        self.__car_speed_max = 40  # только для этого класса

    def show_speed(self):
        if self.get_speed() > self.__car_speed_max:
            print(f"-- ВНИМАНИЕ! текущая скорость движения {self.get_speed()} км/ч "
                  f"превышает ограничение в {self.__car_speed_max} км/ч для данного типа!")
        else:
            print(f"Текущая скорость движения {self.get_speed()} км/ч.")


class SportCar(Car):
    def __init__(self, name, color):
        super().__init__(name, color, is_police=False, type_car='SportСar')
        self.info = "Спортивный авто"
        self.__car_speed_max = 250  # только для этого класса


class PoliceCar(Car):
    def __init__(self, name, color):
        super().__init__(name, color, is_police=True, type_car='PoliceСar')
        self.info = "Полицейский автомобиль"
        self.__car_speed_max = 180  # только для этого класса


t = TownCar('Toyota', 'Gold')
print(f"Инфо: {t.info}")
t.set_turn(turn='left')
t.go(11)
t.set_turn(turn='straight')
t.go(80)
t.show_speed()

w = WorkCar('Kamaz', 'Red')
print(f"Инфо: {w.info}")
w.go(41)
w.show_speed()

s = SportCar('Jaguar', 'Silver')

p = PoliceCar('Niva', 'White')

s.go(-20)

print("\nEnd")
