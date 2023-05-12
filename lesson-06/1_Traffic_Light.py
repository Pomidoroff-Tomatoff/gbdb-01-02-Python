# GeekBrains > Python basics: Oleg Gladkiy (https://geekbrains.ru/users/3837199)
homework_type = "Lesson-6. 1-Traffic-Light"
# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
#    и метод running (запуск). Атрибут реализовать как приватный.
#    В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
#    продолжительность первого состояния (красный) составляет 7 секунд,
#    второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
#    Переключение между режимами должно осуществляться только в указанном порядке:
#    красный, желтый, зеленый. Проверить работу примера, создав экземпляр и вызвав описанный метод.
#    Задачу можно усложнить, реализовав проверку порядка режимов,
#    и при его нарушении выводить соответствующее сообщение и завершать скрипт.
print(homework_type)

import time


class TrafficLight:
    ''' Светофор '''
    __con_color_red =    ""  # "\033[31m"
    __con_color_yellow = ""  # "\033[33m"
    __con_color_green =  ""  # "\033[32m"
    __con_color_reset =  ""  # "\033[0m"
    __con_color_swap =   ""  # "\033[7m"
    __color_list = [('red', 7, __con_color_red), ('yellow', 2, __con_color_yellow), ('green', 5, __con_color_green)]

    # Наверное, нужно два объекта:
    # -- словарь с цветами (ключ) и задержками
    # -- список с последовательностью исполнения по ключу
    # Но эту идею пока не удалось продумать...
    __count = 0
    __max_iteration = 3
    __stop_flag = 0

    def tl_begin(self, start_color='red'):

        if start_color.upper() == 'red'.upper():
            work_order_color = [0, 1, 2, 1]
            print("Начинаем с ", start_color.upper())
        elif start_color.upper() == 'yellow'.upper():
            work_order_color = [1, 2, 1, 0]
            print("Начинаем с ", start_color.upper())
        elif start_color.upper() == 'green'.upper():
            work_order_color = [2, 1, 0, 1]
            print("Начинаем с ", start_color.upper())
        else:
            work_order_color = [0, 1, 2, 1]
            print("Неверно указан цвет, начинаем с красного")

        while self.__count < self.__max_iteration:

            if self.__stop_flag:  # вкл./выкл. светофор, воздействуя другим процессом...
                return

            self.__count += 1
            print(self.__con_color_swap + f"цикл:  {self.__count} (всего {self.__max_iteration})" + self.__con_color_reset)

            for i in work_order_color:
                color, t, con_color = self.__color_list[i]
                print(f"color: {con_color} {color.upper():<10s}{self.__con_color_reset}  задержка: {t}")
                time.sleep(t)



a = TrafficLight()
a.tl_begin("red")

print("End")
