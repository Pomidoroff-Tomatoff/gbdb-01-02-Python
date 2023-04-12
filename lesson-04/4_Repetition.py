# GeekBrains > Python basics: Oleg Gladkiy (https://geekbrains.ru/users/3837199)
homework_type = "Lesson-4. 4_Repetition"
# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
#    Сформировать итоговый массив чисел, соответствующих требованию.
#    Элементы вывести в порядке их следования в исходном списке.
#    Для выполнения задания обязательно использовать генератор.
#    Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
#    Результат: [23, 1, 3, 10, 4, 11]

from random import randint

print(homework_type)

# Генератор списка, решение задания и сервис
any_repeat_gen = lambda el_count: list(randint(1, 101) for i in range(1, el_count+1, 1))  # список случайных элементов
non_repetition = lambda x_list: list(el for el in x_list if x_list.count(el) == 1)        # неповторяющиеся элементы в виде лямбда-функции
repetition_num = lambda x_list: set(el for el in x_list if x_list.count(el) > 1)          # сервис: повторяющиеся эл., мно-во
# -- почему-то, если повторений нет, то возврадается строка "set()"
#    а не пустое множество {}


# Список случайных элементов
SOURCE_LIST_LEN = 10  # задание кол-ва эл-ов в исходном списке

print(f"Выполнение задания для случайного набора числе из {SOURCE_LIST_LEN} элементов")
source_list = any_repeat_gen(SOURCE_LIST_LEN)
destin_list = non_repetition(source_list)
repeat_list = repetition_num(source_list)

print(f"in {len(source_list): 4} any elements: {source_list}")
print(f"to {len(destin_list): 4} non repeat:   {destin_list}")
print(f"   {len(repeat_list): 4} repeat el.:   {repeat_list}")

# Пример, исходный список
print(f"Проверка на примере исходного списка...")
source_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
destin_list = non_repetition(source_list)
repeat_list = repetition_num(source_list)

print(f"in {len(source_list): 4} any elements: {source_list}")
print(f"to {len(destin_list): 4} non repeat:   {destin_list}")
print(f"   {len(repeat_list): 4} el. repeated: {repeat_list}")

print("End")
