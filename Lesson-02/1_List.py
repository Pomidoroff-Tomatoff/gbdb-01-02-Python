# GeekBrains > Python basics: Oleg Gladkiy (https://geekbrains.ru/users/3837199)
homework_type = "Lesson-2. 1-List"
# 1. Создать список и заполнить его элементами различных типов данных.
#    Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
#    Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

print(homework_type)

my_list = [1, 2.123, 'Word', None, complex(2, 10)]
print(f"Data List: {my_list}\n")
index = 0
while index in range(len(my_list)):
    print(f"{index + 1} element «{my_list[index]}», type is {type(my_list[index])}.")
    index += 1

print("End")