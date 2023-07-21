# GeekBrains, Python basics: Oleg Gladkiy (https://geekbrains.ru/users/3837199)
homework_type = "Lesson-5. 5-sum-ALL: МАССОВЫЕ ОПЕРАЦИИ: генерация, запись и чтение"
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

NUMBERS_AMOUNT_MAX = 1000000                          # Количество чисел
SEPARATOR = " "                                       # Разделитель чисел: " ", ",", ";", ";"
module_name = os.path.basename(sys.argv[0])           # Имя этого модуля...
module_name = "".join(module_name.split(".py")[:-1])  # ...и без расширения
DATA_FILENAME = module_name + "__numbers.txt"          # Имя файла данных


# Генерируем и Пишем
with open(DATA_FILENAME, "w+") as file_out:
    '''Генерируем список чисел, объединяем его в строку и пишем в файл на диск'''

    # Генерируем числа
    time_start = time.time()
    numbers = [random.uniform(0, 100) for _ in range(NUMBERS_AMOUNT_MAX)]
    # >>>
    print(f"\rГенер.: {len(numbers)/NUMBERS_AMOUNT_MAX:3.0%}   {len(numbers):,d}   сумма: {sum(numbers):f}   время: {(time.time() - time_start):.2f} с   объём {(sys.getsizeof(numbers)):,d} байт ", end='\n')

    # Пишем
    print(f"\rЗапись...", end=""*5)
    time_start = time.time()
    print(f"{SEPARATOR.join(map(lambda x: f'{x:f}', numbers))}", end="", flush=True, file=file_out)  # str() в 2-а раза медленее...

    # >>> экран
    print(f"\rЗапись: {len(numbers)/NUMBERS_AMOUNT_MAX:3.0%}   {len(numbers):,d}   сумма: {sum(numbers):f}   время: {(time.time() - time_start):.2f} с  ", end='\n')

# Читаем и суммируем
with open(DATA_FILENAME, "r") as file_in:
    '''Читаем сразу всё. Потом вычисляем. Оперативную память не экономим'''
    print(f"\rЧтение ...", end=""*5)
    time_start = time.time()
    numbers = []
    for line in file_in:
        for element in line.split(SEPARATOR):
            if element:
                number = float(element)
                numbers.append(number)
    # >>> экран
    print(f"\rЧтение: {len(numbers)/NUMBERS_AMOUNT_MAX:3.0%}   {len(numbers):,d}   сумма: {sum(numbers):f}   время: {(time.time() - time_start):.2f} с   объём {sys.getsizeof(numbers):,d} байт")
