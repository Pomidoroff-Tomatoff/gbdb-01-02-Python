# GeekBrains > Python basics: Oleg Gladkiy (https://geekbrains.ru/users/3837199)
homework_type = "Lesson-6. 2-Road"
# 2. Реализовать класс Road (дорога), в котором определить атрибуты:
#    length (длина), width (ширина). Значения данных атрибутов должны передаваться
#    при создании экземпляра класса. Атрибуты сделать защищенными.
#    Определить метод расчета массы асфальта, необходимого для покрытия всего
#    дорожного полотна. Использовать формулу: длина * ширина * масса асфальта
#    для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * число см толщины полотна.
#    Проверить работу метода.
#    Например: 20м * 5000м * 25кг * 5см = 12500 т
print(homework_type)


class Road():

    def __init__(self, length: float = 0, width: float = 0):
        self.__length = length            # metre
        self.__width = width              # metre
        self.__thickness = 5              # см
        self.__mass_on_1_thickness = 25   # кг

    def mass(self):
        road_length = self.__length
        road_width = self.__width

        mass_asphalt = self.__mass_on_1_thickness * self.__thickness * road_length * road_width
        print(f"Дорожное покрытие: ширина {road_width} м; длина {road_length} м; масса {mass_asphalt:,d} кг")
        return mass_asphalt


r1 = Road(length=5000, width=20)
r1.mass()
r2 = Road(length=1, width=1)
r2.mass()

print("End")
