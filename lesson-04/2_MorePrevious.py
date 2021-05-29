# GeekBrains > Python basics: Oleg Gladkiy (https://geekbrains.ru/users/3837199)
homework_type = "Lesson-4. 2-MorePrevious"
# 2. Представлен список чисел. Необходимо вывести элементы исходного списка,
#    значения которых больше предыдущего элемента.
#    Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
#    Для формирования списка использовать генератор.
#    Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
#    Результат: [12, 44, 4, 10, 78, 123].

from random import randint

print(homework_type)


# Генератор списка в виде функции
def gen_list_random(i_start=0, i_end=10, i_step=1):
    gen_list = []
    for i in range(i_start, i_end, i_step):
        gen_list.append(randint(0, 101))
    return gen_list

# Преобразователь списка в виде функции
def more_previous(source_list):
    destin_list = []
    for i in range(1, len(source_list)):
        if source_list[i] > source_list[i - 1]:
            destin_list.append(source_list[i])
    return destin_list


print("A. Генератор и преобразование списка ввиде функций:")
source_list = gen_list_random(1, 1000, 100)
destin_list = more_previous(source_list)
print(f"in: {source_list}")
print(f"to: {destin_list}")

print("Б. Генератор и преобразование списка в видке спискового включения (list comprehension):")
source_list = [randint(0, 101) for i in range(1, 1000, 100)]
destin_list = [source_list[i] for i in range(1, len(source_list)) if source_list[i] > source_list[i - 1]]
print(f"in: {source_list}")
print(f"to: {destin_list}")


print("End")
