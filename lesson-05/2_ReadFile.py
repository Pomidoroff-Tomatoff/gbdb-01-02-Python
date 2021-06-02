# GeekBrains > Python basics: Oleg Gladkiy (https://geekbrains.ru/users/3837199)
homework_type = "Lesson-5. 2-ReadFile"
# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
#    выполнить подсчет количества строк, количества слов в каждой строке.

print(homework_type)

import sys
import os

data_file_name = "2_ReadFile_DATA_handmade.txt"

with open(data_file_name, "r", encoding="utf-8") as data_file:
    line_count_max = 10
    line_count = 0
    word_count = 0
    word_list = []
    print(f"Строки файла «{data_file_name}»:\n")
    for in_str in data_file:
        in_str = in_str.replace('\n', '')   # удаляем символ перевода строки
        in_str = in_str.replace('  ', ' ')  # удаляем двойные пробелы
        word_list = in_str.split(' ')  # разделяем на слова (по пробелу) и помещаем в списко
        word_count += len(word_list)
        line_count += 1
        print(" ".join(word_list))
        # print(word_list)

    print("")
    print(f"Всего строк в файле: {line_count}")
    print(f"Всего слов в файле:  {word_count}")


print("End")