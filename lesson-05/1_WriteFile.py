# GeekBrains > Python basics: Oleg Gladkiy (https://geekbrains.ru/users/3837199)
homework_type = "Lesson-5. 1-WriteFile"
# 1. Создать программно файл в текстовом формате, записать в него построчно данные,
#    вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

print(homework_type)

with open("1_WriteFile_DATA_program.txt", "w", encoding="utf-8") as data_file:

    print("Введите строку данных или Enter для звершения: ")

    line_count_max = 10
    line_count = 0

    while line_count < line_count_max:
        line_count += 1
        in_str = input(f"Line {line_count: 2d}>> ")
        if in_str == "" or in_str == " ":  # проверяем на пустую строку или пробел (только один)
            break
        else:
            print(in_str, file=data_file)
            # data_file.write(in_str + "\n")

    print("Ввод завершён")


print("End")