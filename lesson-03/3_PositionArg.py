# GeekBrains > Python basics: Oleg Gladkiy (https://geekbrains.ru/users/3837199)
homework_type = "Lesson-3. 3_PositionArg"
# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
#    и возвращает сумму наибольших двух аргументов.

print(homework_type)


def my_func(num_1, num_2, num_3):
    my_list = [num_1, num_2, num_3]
    print(f"--source parameter: {my_list}")
    my_list.sort(reverse=True)
    print(f"--sorted parameter: {my_list}")
    return my_list[0] + my_list[1]


print(f"Сумма двух наибольших значений параметров: {my_func(1, 8, 3)}")
print(f"Сумма двух наибольших значений параметров: {my_func(15, 1, 10)}")

print("End")
