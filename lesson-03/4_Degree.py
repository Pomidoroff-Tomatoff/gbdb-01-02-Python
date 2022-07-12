# GeekBrains > Python basics: Oleg Gladkiy (https://geekbrains.ru/users/3837199)
homework_type = "Lesson-3. 3_PositionArg"
# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
#    Необходимо выполнить возведение числа x в степень y.
#    Задание необходимо реализовать в виде функции my_func(x, y).
#    При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
#    Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
#    Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

print(homework_type)

def my_func(x, y):
    return x**y


def my_func_handmade(x, y):
    num_result = 1
    if x == 0 and y == 0:
        return None
    if x != 0 and y == 0:
        return 1
    if x == 0 and y != 0:
        return 0

    for i in range(abs(y)):
        num_result = num_result * x
    if y < 0:
        num_result = 1 / num_result
    return num_result


print(f"Результат возведения в степень: {my_func(10, -3)}  -- встроенный функционал")
print(f"Результат возведения в степень: {my_func_handmade(10, -3)}  -- ручные расчёты")

print("End")
