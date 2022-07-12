# GeekBrains > Python basics: Oleg Gladkiy (https://geekbrains.ru/users/3837199)
homework_type = "Lesson-4. 7_GenFactorial"
# 7. Реализовать генератор с помощью функции с ключевым словом yield,
#    создающим очередное значение. При вызове функции должен создаваться объект-генератор.
#    Функция должна вызываться следующим образом: for el in fact(n).
#    Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел,
#    начиная с 1! и до n!.
#    Подсказка: факториал числа n — произведение чисел от 1 до n.
#    Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

print(homework_type)

def fact(n_end: int):
    i = 1
    n = 1
    while i <= n_end:
        n = n * i
        i += 1
        yield n

n = 10
source_list = [i for i in fact(n)]

print(f"{len(source_list)} elements in list n!:\n{source_list}")

print("End")
