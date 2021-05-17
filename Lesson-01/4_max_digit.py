# GeekBrains > Python basics: Oleg Gladkiy (https://geekbrains.ru/users/3837199)
# Lesson-1. 4-Max-Digit
# 4. Пользователь вводит целое положительное число.
#    Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.


n = input("Введите целое число: ")
n_max = 0
index = 0
while index < len(str(n)):
    if n_max < int(n[index]):
        n_max = int(n[index])
    index += 1

print("Maximum digit is ", n_max)
