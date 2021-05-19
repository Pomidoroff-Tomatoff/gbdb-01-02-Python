# GeekBrains > Python basics: Oleg Gladkiy (https://geekbrains.ru/users/3837199)
homework_type = "Lesson-2. 2-List-swap"
# 2. Для списка реализовать обмен значений соседних элементов,
#    т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
#    При нечетном количестве элементов последний сохранить на своем месте.
#    Для заполнения списка элементов необходимо использовать функцию input().

print(homework_type)

my_list = input("Введите строку значений разделённых пробелом: ")
my_list = my_list.split(" ")

print(f"Data List A: {my_list}")

# Swap elements in list
index = 0
while index < (len(my_list) - 1):
    my_list[index], my_list[index + 1] = my_list[index + 1], my_list[index]
    index += 2

print(f"Data List B: {my_list}")

print(f"End")