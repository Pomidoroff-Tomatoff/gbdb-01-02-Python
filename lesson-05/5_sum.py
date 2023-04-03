# GeekBrains, Python basics: Oleg Gladkiy (https://geekbrains.ru/users/3837199)
homework_type = "Lesson-5. 5-sum-ALL: пишем и читаем числа сразу всем списком"
''' Задание №:
5.  Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
    Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
    Решение:
    -- Пишем и читаем сразу весь массив данных.
    -- Особенности: 
       > расточительное использование памяти; 
       > высокая скорость, если достаточно памяти.
       > работает втихую, информируя только по завершению операции '''
print("\n" + homework_type + "\n")

import os, sys, random, time

NUMBERS_AMOUNT_MAX = 100000                       # Количество чисел
SEPARATOR = " "                                       # Разделитель чисел: " ", ",", ";", ";"
module_name = os.path.basename(sys.argv[0])           # Имя этого модуля...
module_name = "".join(module_name.split(".py")[:-1])  # ...и без расширения
DATA_FILENAME = module_name + "_numbers.txt"          # Имя файла данных


def gen_numbers(count=NUMBERS_AMOUNT_MAX):
    ''' Генератор чисел '''
    for i in range(count):
        yield round(random.uniform(0, 100), 2)


# Пишем.
with open(DATA_FILENAME, "w+") as file_out:
    '''Создаём список, объединяем его в строку и сразу пишем в файл на диск'''
    time_start = time.time()
    numbers = list(gen_numbers())  # список всех чисел
    print(f"{SEPARATOR.join(map(str, numbers))}", end="", flush=True, file=file_out)

    # >>> на экран:
    print(f"Запись: {len(numbers)/NUMBERS_AMOUNT_MAX:3.0%}   {len(numbers):,d}   сумма: {sum(numbers):.2f}   время: {(time.time() - time_start):.2f} с")

# Читаем и считаем
with open(DATA_FILENAME, "r") as file_in:
    '''Читаем сразу всё. Так же вычисляем. Память не экономим'''
    time_start = time.time()
    numbers = []
    for line in file_in:
        for element in line.split(SEPARATOR):
            if element:
                number = round(float(element), 2)
                numbers.append(number)

    # >>> на экран:
    print(f"Чтение: {len(numbers)/NUMBERS_AMOUNT_MAX:3.0%}   {len(numbers):,d}   сумма: {sum(numbers):.2f}   время: {(time.time() - time_start):.2f} с")
