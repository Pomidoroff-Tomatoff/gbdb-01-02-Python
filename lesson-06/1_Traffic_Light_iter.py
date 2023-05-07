# GeekBrains > Python basics: Oleg Gladkiy (https://geekbrains.ru/users/3837199)
homework_type = "Lesson-6. 1-Traffic-Light as Iterator-class"
# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
#    и метод running (запуск). Атрибут реализовать как приватный.
#    В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
#    продолжительность первого состояния (красный) составляет 7 секунд,
#    второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
#    Переключение между режимами должно осуществляться только в указанном порядке:
#    красный, желтый, зеленый. Проверить работу примера, создав экземпляр и вызвав описанный метод.
#    Задачу можно усложнить, реализовав проверку порядка режимов,
#    и при его нарушении выводить соответствующее сообщение и завершать скрипт.

#    Решение: класс как итератор
print(homework_type)
import time, itertools


class TrafficLights:
    ''' Светофор
        -- перебор цвета огней: итератор-класс
        -- информирмирование о цвете: метод + магический метод __call__
    '''
    __RED = "r"                         # Для удобства...
    __YEL = "y"                         # ключи доступа к словарям огней светофора
    __GRN = "g"
    __colorcode_RED = "\033[31m"     # Команды включения огня светофора
    __colorcode_YEL = "\033[33m"     # и, по совместительству,
    __colorcode_GRN = "\033[32m"     # esc-последовательности управления цветом (текста или фона)
    __colorcode_reset="\033[0m"      # в консоли.
    __colorcode_swap ="\033[7m"
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
    # Порядок следования цветов огней светофора
    __keys = [__RED, __YEL, __GRN, __YEL,]

    def __init__(self, start_color: str = __RED):
        self.current_color_name = ""    # текущие огни запущенного светофора
        self.current_glow_time = 0      # или значения используемого
        self.current_colorcode = ""     # итератора класса

        self.start_color = start_color.upper()
        if False:
            pass  # для удобства чтения и красоты...

        elif self.start_color == self.__RED.upper() or \
             self.start_color == self.__colors[self.__RED]['name'].upper():

            self.__key_index_start = 0

        elif self.start_color == self.__GRN.upper() or \
             self.start_color == self.__colors[self.__GRN]['name'].upper():

            self.__key_index_start = -2

        elif self.start_color == self.__YEL.upper() or \
             self.start_color == self.__colors[self.__YEL]['name'].upper():

            self.__key_index_start = -1

        else:
            raise ValueError("Ошибка задания начального цвета огня Светофора.")

    def __iter__(self):
        self.__keys_iter = self.circle(iterable=self.__keys, start=self.__key_index_start)
        for key in self.__keys_iter:
            self.current_glow_time =  self.__colors[key]['glow_time']
            self.current_color_name = self.__colors[key]['name']
            self.current_colorcode =  self.__colors[key]['colorcode']
            yield self.current_color_name, \
                  self.current_glow_time, \
                  self.current_colorcode
            time.sleep(self.current_glow_time)

    def __next__(self):
        ''' не получиться ПОСЛЕ оператора RETURN c командой включения цвета светофора
            установить задержку свечения этого цвета:
            -- после return всё будет проигнорировано!
        '''
        key = next(self.__keys)
        return key     # здесь yield нельзя!
        time.sleep(1)  # не будет выполняться после return

    def __call__(self):
        return self.get_light_info()

    def __str__(self):
        return self.get_light_info()

    def get_light_info(self):
        return f"{self.current_colorcode}{self.current_color_name.upper():<10s}{self.__colorcode_reset} " + \
               f" время свечения: {self.current_glow_time} секунд"

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

tl = TrafficLights("G")
for i, values in enumerate(tl, start=1):
    color_name, glow_time, colorcode = values
    if i >12: break
    print(f"{i:03d} " + tl(), end="\n")

print("End")
