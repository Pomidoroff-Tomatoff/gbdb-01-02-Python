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
    __colorcode_GRN = "\033[32m"     # esc-последовательности управления цветом текстом (фона)
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
        self.start_color = start_color
        if  start_color.upper() == self.__RED.upper() or \
            start_color.upper() == self.__colors[self.__RED]['name'].upper():
            keys = []
        elif start_color.upper() == self.__GRN.upper() or \
             start_color.upper() == self.__colors[self.__GRN]['name'].upper():
            keys = [self.__GRN, self.__YEL]
        elif start_color.upper() == self.__YEL.upper() or \
             start_color.upper() == self.__colors[self.__YEL]['name'].upper():
            keys = [self.__YEL]
        else:
            raise ValueError("Ошибка задания начального цвета огня Светофора.")

        keys.extend(self.__keys)                  # к стартовой послед-ти + основную...
        self.__keys_iter = itertools.cycle(keys)  # бесконечный итератор по ключам

        self.current_color_name = ""              # текущие огни запущенного светофора
        self.current_glow_time = 0                # или значения используемого
        self.current_colorcode = ""               # итератора класса

    def __iter__(self):
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

    pass  # TrafficLights


# Поехали

tl = TrafficLights("Y")                     # создаём итератор-класс
for i, values in enumerate(tl, start=1):
    if i > 5: break
    print(f"{i:03d} " + tl(), end="\n")

print("End")
