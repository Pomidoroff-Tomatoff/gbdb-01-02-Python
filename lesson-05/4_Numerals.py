# GeekBrains > Python basics: Oleg Gladkiy (https://geekbrains.ru/users/3837199)
homework_type = "Lesson-5. 4_Numerals"
# 4. Создать (не программно) текстовый файл со следующим содержимым:
#      One — 1
#      Two — 2
#      Three — 3
#      Four — 4
#    Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
#    При этом английские числительные должны заменяться на русские.
#    Новый блок строк должен записываться в новый текстовый файл.

print(homework_type)

import sys


file_in_name \
    = "4_Numerals__list_en_handmade.txt"
file_out_name \
    = "4_Numerals__list_ru.txt"
long_dash_symbol = '—'

numbers = {
    '0': ['zero', 'ноль'],
    '1': ['one', 'один'],
    '2': ['two', 'два'],
    '3': ['three', 'три'],
    '4': ['four', 'четыре'],
    '5': ['five', 'пять'],
    '6': ['six', 'шесть'],
    '7': ['seven', 'семь'],
    '8': ['eight', 'восемь'],
    '9': ['nine', 'девять']
}


def special_symbol_remover(str):
    bad_symbol_list = ['\n', '\r', '\t', '-', '–', '—',
                       '\ufeff']  # Последнее сл. слово добавляет Блокнот под Windows...
    for bad_symbol in bad_symbol_list:
        while str.find(bad_symbol) >= 0:
            str = str.replace(bad_symbol, '')

    while str.find('  ') >= 0:
        str = str.replace('  ', ' ')  # все двойные пробелы заменяем на одинарные

    str = str.strip()  # удаление пробелов в начале и конце строки

    return str


with open(file_in_name, "r", encoding="utf-8") as file_in:
    with open(file_out_name, "w", encoding="utf-8") as file_out:
        print("Прочитаны данные:")
        for str_in in file_in:
            str_in = special_symbol_remover(str_in)  # чистим строку
            str_in_list = str_in.split(' ')          # получаем список элементов одной стоки

            try:
                num_key = str(str_in_list[1])            # цифра
                num_en, num_ru = numbers.get(num_key)    # числительные
                for output_strim in [sys.stdout, file_out]:  # выводит на экран и в файл
                    print(f"{num_ru.capitalize()} {long_dash_symbol} {num_key}", file=output_strim)

            except:
                print("ОШИБКА ФОРМАТА -- нечитаемые служебные символы...")

print("End")
