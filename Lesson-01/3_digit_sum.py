# GeekBrains > Python basics: Oleg Gladkiy (https://geekbrains.ru/users/3837199)
# Lesson-1. 3-Digit-Summary
# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
#    Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.


n = int(input ("Введите целое число: "))
nn = int(str(n) + str(n))
# print(nn)
nnn = int(str(nn) + str(n))
# print(nnn)
n_sum = n + nn + nnn

print("n + nn + nnn = ", n_sum)
