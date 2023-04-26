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

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position  # должность
        self.__income = {'wage': 0, 'bonus': 0}  # доход

    def _set_income_wage(self, wage=0):
        self.__income['wage'] = wage

    def _set_income_bonus(self, bonus=0):
        self.__income['bonus'] = bonus

    def _get_income_wage(self):
         return self.__income['wage']

    def _get_income_bonus(self):
         return self.__income['bonus']


class Position(Worker):
    def __init__(self, name, surname, position):
        super().__init__(name, surname, position)

    def set_total_income(self, wage=0, bonus=0):
        self._set_income_wage(wage=wage)
        self._set_income_bonus(bonus=bonus)

    @property
    def get_total_income(self, ):
        return self._get_income_wage() + self._get_income_bonus()

    @property
    def get_full_name(self):
        return self.name + ' ' + self.surname


w = Position("Иван", "Петров", "продавец")
w.set_total_income(wage=1000, bonus=100)

print(f"{'Полное имя работника:':<25s} «{w.get_full_name}»")
print(f"{'Общий доход работника:':<25s} {w.get_total_income} р")


print("End")
