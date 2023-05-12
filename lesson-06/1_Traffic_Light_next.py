
# GeekBrains > Python basics: Oleg Gladkiy (https://geekbrains.ru/users/3837199)
homework_type = "Lesson-6. 1-Traffic-Light as Iterator-class with __next__"
# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
#    и метод running (запуск). Атрибут реализовать как приватный.
#    В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
#    продолжительность первого состояния (красный) составляет 7 секунд,
#    второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
#    Переключение между режимами должно осуществляться только в указанном порядке:
#    красный, желтый, зеленый. Проверить работу примера, создав экземпляр и вызвав описанный метод.
#    Задачу можно усложнить, реализовав проверку порядка режимов,
#    и при его нарушении выводить соответствующее сообщение и завершать скрипт.

#    Решение: класс как итератор-генератор
#       __iter__ только интерфейс
#       __next__ только отдаём параметры, временные задержки не генерируются!!!
#    Внимание!
#       Временные задержки, как в часах, не генерируются. Используйте задержку в коде вне экз. класса.
#       НЕ УЧИТЫВАЕТСЯ ВРЕМЯ!!!

print(homework_type)
import time, itertools


class TrafficLights:
    ''' Светофор
        -- перебор цвета огней: итератор-класс
        -- информирование о цвете: метод + магический метод __call__
    '''
    __RED = "r"                         # Для удобства...
    __YEL = "y"                         # ключи доступа к словарям огней светофора
    __GRN = "g"
    __colorcode_RED = "\033[31m"     # Команды включения огня светофора
    __colorcode_YEL = "\033[33m"     # и, по совместительству,
    __colorcode_GRN = "\033[32m"     # esc-последовательности управления цветом (текста или фона)
    __colorcode_reset="\033[0m"      # в консоли.
    __colorcode_swap ="\033[7m"
    # Библиотека цветов
    __colors = {
        __RED: {
            'name': 'RED',
            'glow_time': 7,
            'colorcode': __colorcode_RED},
        __YEL: {
            'name': 'YELLOW',
            'glow_time': 2,
            'colorcode': __colorcode_YEL},
        __GRN: {
            'name': 'GREEN',
            'glow_time': 5,
            'colorcode': __colorcode_GRN}
    }
    # Список следования цветов:
    # -- перемешиваем...
    __color_order_main = [__RED, __GRN,]    # основные цвета
    __color_order_serv = [__YEL,]           # разделительный цвет
    __color_order = [color
        for pair in zip(__color_order_main, itertools.repeat(__color_order_serv[0]))
        for color in pair]

    def __init__(self, start_color: str = __RED):
        self.current_color_key = ""     # ключ текущие света работающего экз. светофора

        # Проверяем входящий параметр и инициализируем индекс первого цвета в списке следования
        if not start_color:
            start_color = self.__RED

        start_color = start_color.upper()
        color_keys  = list(map(lambda key: key.upper(), self.__colors.keys()))
        color_names = list(map(lambda key: self.__colors[key]['name'].upper(), self.__colors.keys()))
        if start_color in color_keys:
            self.__key_index_start = color_keys.index(start_color)
        elif start_color in color_names:
            self.__key_index_start = color_names.index(start_color)
        else:
            raise ValueError(f"Ошибка задания начального цвета огня Светофора." + " " + \
                             f"Используйте {list(color_keys)} или {list(color_names)}.")

        # итератор по ключам в бесконечном цикле
        self.__keys_iter = self.circle(iterable=self.__color_order, start=self.__key_index_start)

    def __iter__(self):
        return self

    def __next__(self):
        ''' генератор параметров для светофоро:
            -- временная задержка не устанавливается
            -- после return всё будет проигнорировано!
            -- здесь yield использовать нельзя!
        '''
        key = next(self.__keys_iter)
        self.current_color_key = key
        return self.__colors[key]['name'], \
               self.__colors[key]['glow_time'], \
               self.__colors[key]['colorcode']

    def __call__(self):
        return self.get_light_info()

    def __str__(self):
        return self.get_light_info()

    def __set_light_info(self, key: str = ""):
        self.current_color_key = key
        return self.__colors[key]['name'], self.__colors[key]['glow_time'], self.__colors[key]['colorcode']

    def get_light_info(self):
        key = self.current_color_key
        return f"{self.__colors[key]['colorcode']}" + \
               f"{self.__colors[key]['name'].upper():<10s}" + \
               f"{self.__colorcode_reset}" + " " + \
               f" время свечения: {self.__colors[key]['glow_time']} секунд"

    def circle(self, iterable: list = [], start: int = 0):
        ''' бесконечный цикл по последовательности с указанием начального элемента в первом цикле '''
        if (length := len(iterable)) > 0:
            if start >= 0:
                if not start < length:
                    start = (start + 1) % length - 1
            else:
                if -start > length:
                    start = start % length * (-1)
        else:  # пустой список!!!
            return None  # нам нечего перечислять -- останавливаемся.

        index = start

        while True:
            index = 0 if not index < len(iterable) else index
            yield iterable[index]
            index += 1

        pass  # cycle

    pass  # TrafficLights


# Поехали!
# создаём итератор-класс и... огоньки зажигайтесь!

tl = TrafficLights('y')
for i, color_parameters in enumerate(tl, start=1):
    color_name, glow_time, colorcode = color_parameters
    if i > 12: break
    print(f"{i:03d} " + tl(), end="\n")
    time.sleep(glow_time)


print("End")
