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

with open("6_dict_DATA_handmade.txt", 'r', encoding="utf-8") as file_in:  # "windows-1251"
    school = dict()
    for string in file_in:

        # Ищем посимвольно название учебного предмета в начале строки

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
            if char.isdigit():
                chars.extend(char)
            else:
                number = ''.join(chars)
                chars = []
                if number and not number.isspace():
                    numbers.append(int(number))
        else:
            if len(chars):
                number = ''.join(chars)
                numbers.append(int(number))
                chars = []

        # Суммируем найденные учебные часы
        # и записываем их в словарь по названию предмета (ранее найденного)

        school[course_name] = sum(numbers)

# >>> РЕЗУЛЬТАТ
for name, hours in school.items():
    print(f"{name[:20:]:<20s}{hours:>5d}")
