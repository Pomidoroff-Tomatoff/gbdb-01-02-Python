# GeekBrains > Python basics: Oleg Gladkiy (https://geekbrains.ru/users/3837199)
homework_type = "Lesson-6. 3-Worker"
# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
#    name, surname, position (должность), income (доход). Последний атрибут должен быть
#    защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
#    например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность)
#    на базе класса Worker. В классе Position реализовать методы получения
#    полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
#    Проверить работу примера на реальных данных (создать экземпляры класса Position,
#    передать данные, проверить значения атрибутов, вызвать методы экземпляров).
print(homework_type)


class Worker:

    __income = {'wage': 0, 'bonus': 0}  # доход

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position  # должность


    def set_income(self, wage, bonus):
        self.__income['wage'] = wage
        self.__income['bonus'] = bonus

    def get_income(self):
         return  self.__income['wage'] + self.__income['bonus']


class Position(Worker):
    def __init__(self, name, surname, position):
        super().__init__(name, surname, position)

    def full_name(self):
        return self.name + ' ' + self.surname



w = Position("Иван", "Петров", "продавец")
w.set_income(1000, 100)

print(f"Полное имя работника: «{w.full_name()}»")
print(f"Доход работника: {w.get_income()} р")


print("End")
