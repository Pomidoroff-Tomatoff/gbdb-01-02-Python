# GeekBrains > Python basics: Oleg Gladkiy (https://geekbrains.ru/users/3837199)
homework_type = "Lesson-6. 5_Stationery"
# 5. Реализовать класс Stationery (канцелярская принадлежность).
#    Определить в нем атрибут title (название) и метод draw (отрисовка). Метод выводит
#    сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
#    Handle (маркер). В каждом из классов реализовать переопределение метода draw.
#    Для каждого из классов методы должен выводить уникальное сообщение.
#    Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
print(homework_type)


class Stationery:

    def __init__(self, title=None):
        self.__title = title

    def set_title(self, title=""):
        self.__title = title

    def get_title(self):
        return self.__title

    def draw(self):
        print(f"Запуск отрисовки.")


class Pen(Stationery):
    def __init__(self):
        super().__init__(title='Карандаш')

    def draw(self):
        print(f"Запускаем отрисовку линии меняющейся толщины при помощи принадлежности «{self.get_title()}»")


class Pencil(Stationery):
    def __init__(self):
        super().__init__(title='Ручка')

    def draw(self):
        print(f"Рисую ТОНКУЮ линию при помощи принадлежности \"{self.get_title()}\".")


class Handle(Stationery):
    def __init__(self):
        super().__init__(title='Маркер')

    def draw(self):
        print(f"Выполняю выделение принадлежностью \"{self.get_title()}\".")


p_1 = Pen()
p_1.draw()

p_2 = Pencil()
p_2.draw()

h = Handle()
h.draw()


print("End")
