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
    __length = 0  # metre
    __width = 0   # metre
    __thickness = 5  # см
    __mass_on_1_thickness = 25  # кг

    def mass(self, road_width=20, road_length=5000):
        print(f"Дорожное покрытие: ширина {road_width} м, длина {road_length} м")
        mass_asphalt = self.__mass_on_1_thickness * self.__thickness * road_length * road_width
        print(f"--расчётная масса асфальта: {mass_asphalt} кг")
        return mass_asphalt


r = Road()
r.mass(1, 1)
r.mass()

print("End")
