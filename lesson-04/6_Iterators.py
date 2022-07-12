# GeekBrains > Python basics: Oleg Gladkiy (https://geekbrains.ru/users/3837199)
homework_type = "Lesson-4. 6_Iterator_A"
# 6. Реализовать два небольших скрипта:
#    а) итератор, генерирующий целые числа, начиная с указанного,
#    б) итератор, повторяющий элементы некоторого списка, определенного заранее.
#    Подсказка: использовать функцию count() и cycle() модуля itertools.
#               Обратите внимание, что создаваемый цикл не должен быть бесконечным.
#               Необходимо предусмотреть условие его завершения.
#    Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
#    Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

print(homework_type)

import itertools

# итератор-генератор нечётных чисел
def num_gen_iterator(i_start, i_finish):
    for i in itertools.count(i_start):
        if i > i_finish:
            break
        else:
            yield i * 2 - 1


# итератор перебора значений в наборе
def elements_enumerator(src_lst: list, iter_max: int):
    i = 0
    for element in itertools.cycle(src_lst):
        if i >= iter_max:
            break
        else:
            yield element
            i += 1


num_list_start: int = 1
num_list_end = 10
max_enum = 25

# Получаем набор из нечётных чисел с использованием итератора num_gen_iterator
source_list = list(i for i in num_gen_iterator(num_list_start, num_list_end))
# перебераем этот набор при помощи ит-ра elements_enumerator с ограничением
destin_list = list(i for i in elements_enumerator(source_list, max_enum))

print(f"Получен набор нечётных чисел от {num_list_start} до {num_list_end}:")
print(f"  {len(source_list)} el. in {source_list}")
print(f"Перебор списка... но не более {max_enum} итераций:")
print(f"  {len(destin_list)} el. in {destin_list}")

print("End")
