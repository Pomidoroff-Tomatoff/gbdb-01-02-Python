# GeekBrains, Python basics: Oleg Gladkiy (https://geekbrains.ru/users/3837199)
homework_type = "Lesson-5. 6-dict: Словарная работа"
''' Задание №:
6.  Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
    и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
    Важно, чтобы для каждого предмета не обязательно были все типы занятий.
    Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
    Вывести словарь на экран.

    Примеры строк файла:
        Информатика: 100(л) 50(пр) 20(лаб).
        Физика: 30(л) — 10(лаб)
        Физкультура: — 30(пр) —
    Пример словаря:
        {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30} '''
print("\n" + homework_type + "\n")

# Учебные предметы

with open("6_dict_DATA_handmade.txt", 'r', encoding="utf-8") as file_in:  # "windows-1251" "utf-8"
    school = dict()
    # for string in file_in:
    while string := file_in.readline():

        # Проверяем строку на пустую, удаляем непечатные спецсимволы.
        # Если строка путая, то пропускаем итерацию

        chars = []
        for char in string:
            if char.isprintable():                    # Пропускаем непечатные спец-символы (к ним относится определние кодировки в начале файла)
                chars.append(char)
        string = "".join(chars)
        if not string or string.isspace():            # Пропускаем итерацию в цикле
            continue

        # Ищем посимвольно название учебного предмета
        # в начале строки

        chars = []
        for index, char in enumerate(string, start=0):
            if char.isalpha() or char.isspace():
                chars.extend(char)
            else:
                next_start = index
                break

        course_name = "".join(chars).strip()

        # Ищем посимвольно отведённые на учебный предмет часы
        # в продолжении строки

        chars = []
        numbers = []
        for char in string[next_start::]:
            if char.isdigit():                        # Цифра
                chars.extend(char)                    # - накапливаем цифры в список
            else:                                     # Разделитель чисел -- всё, что не цифра
                number = ''.join(chars)               # - объединяем список цифр в числовую строку
                chars = []                            # - сбрасываем список цифр в исходное
                if number and not number.isspace():   # проверка числа
                    numbers.append(int(number))       # - конвертируем строку цифр в числовой тип
        else:                                         # Разделитель чисел -- конец строки
            if len(chars):                            # - если список цифр не пуст
                number = ''.join(chars)               # - объединяем их в число-строку
                numbers.append(int(number))           # - конвертируем числовой тип и добаляем в список найденных цифровыз значений
                chars = []                            # - сбрасываем список цифр в исходное (не обязательно)

        # Суммируем найденные учебные часы
        # и записываем их в словарь по названию предмета (ранее найденного)

        school[course_name] = sum(numbers)


# >>> РЕЗУЛЬТАТ
print(f"Словарь как есть: \n{school}\n")
print(f"Словарь построчно \"ключ-значение\":")
for name, hours in school.items():
    print(f"{name[:20:]:<20s}{hours:>5d}")
