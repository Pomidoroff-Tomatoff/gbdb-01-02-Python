# GeekBrains, Python basics: Oleg Gladkiy (https://geekbrains.ru/users/3837199)
homework_type = "Lesson-5. 5-sum-ALL: индивидуальная запись-чтение каждого числа"
''' Задание №:
5.  Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
    Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
    Решение:
    -- Пишем и читаем каждое число индивидуально.
    -- Особенности: 
       > очень экономное использование памяти -- только на одно число;
       > можно обработать очень большие объёмы чисел, ограничиваясь только дисковым пространством 
       > низкая скорость, которая сильно зависит от кэша дисковой системы
       > работает открыто информируя о состоянии дел в текущий момент времени '''
print("\n" + homework_type + "\n")

import os, sys, random, time

NUMBERS_AMOUNT_MAX = 100000                          # Количество чисел
SEPARATOR = " "                                       # Разделитель чисел: " ", ",", ";", ";"
module_name = os.path.basename(sys.argv[0])           # Имя этого модуля...
module_name = "".join(module_name.split(".py")[:-1])  # ...и без расширения
DATA_FILENAME = module_name + "_numbers.txt"          # Имя файла данных


def gen_numbers(count=NUMBERS_AMOUNT_MAX):
    ''' Генератор чисел '''
    for i in range(count):
        yield round(random.uniform(0, 100), 2)


def get_number(file_name=DATA_FILENAME):
    ''' Генератор чисел из файлового потока '''
    global SEPARATOR
    with open(file_name, "r") as file_in:
        symbols = []
        while symbol := file_in.read(1):
            if symbol == SEPARATOR:
                yield round(float("".join(symbols)), 2)
                symbols = []
            else:
                symbols.extend(symbol)
        else:
            return None


# Пишем по одному сгенерированному числу
with open(DATA_FILENAME, "w+") as file_out:
    '''Пишем по одному значению'''
    numbers_sum = 0
    time_start = time.time()
    for i, number in enumerate(gen_numbers(), start=1):       # генерируем число в цикле
        numbers_sum += number                                 # сумма чисел для контроля качества кода!
        print(f"{number:.2f}", end=SEPARATOR, file=file_out)  # >>> в файл на диск:
        # >>> экран
        print(f"\rЗапись: {i/NUMBERS_AMOUNT_MAX:>4.0%}   {i:>10,d}   сумма: {numbers_sum:.2f}   время: {(time.time()-time_start):.2f} с", end=' '*5)
    print(flush=True, file=file_out)                          # сбросим кэш диска
    print()

# Читаем и подсчитываем
time_start = time.time()
numbers_sum = 0
for i, number in enumerate(get_number(DATA_FILENAME), start=1):
    numbers_sum += number
    # >>> экран:
    print(f"\rЧтение: {i / NUMBERS_AMOUNT_MAX:>4.0%}   {i:>10,d}   сумма: {numbers_sum:.2f}   время: {(time.time() - time_start):.2f} с",  end=' '*5)

print()
