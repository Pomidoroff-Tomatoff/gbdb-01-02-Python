# GeekBrains > Python basics: Oleg Gladkiy (https://geekbrains.ru/users/3837199)
homework_type = "Lesson-3. 1-Division"
# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
#    Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

print(homework_type)


def str_to_digit(number_as_string):
    try:
        my_number = float(number_as_string)
    except ValueError:
        my_number = None
        print("Digital Error")
    return my_number


def my_func_division(a, b):
    if b == 0:
        print("Ошибка делителя: на ноль делить нельзя")
        return None
    return a / b


number_a = str_to_digit(input("Ведите 1-ое число: "))
if number_a is not None:
    number_b = str_to_digit(input("Ведите 2-ое число: "))
    if number_b is not None:
        result_number = my_func_division(number_a, number_b)
        if result_number is not None:
            print(f"Результат деления: {result_number}")

print("End")
