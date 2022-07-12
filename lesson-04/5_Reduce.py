# GeekBrains > Python basics: Oleg Gladkiy (https://geekbrains.ru/users/3837199)
homework_type = "Lesson-4. 5_Reduce"
# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
#    В список должны войти четные числа от 100 до 1000 (включая границы).
#    Необходимо получить результат вычисления произведения всех элементов списка.
#    Подсказка: использовать функцию reduce().
print(homework_type)

from functools import reduce

i_min = 100
i_max = 1000

source_list_gen = lambda el_min, el_max: list(el for el in range(el_min, el_max + 1, 1) if el % 2 == 0)
multiplication = lambda el, el_next: el * el_next

source_list = source_list_gen(i_min, i_max)
result_fact = reduce(multiplication, source_list)

print(f"{len(source_list)} elements: {source_list}")
print(f"Multiplication = {result_fact:,}.")

print("End")
