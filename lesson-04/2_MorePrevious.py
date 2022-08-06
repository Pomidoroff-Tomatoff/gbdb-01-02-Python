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


# Генератор (функция-генератор)
def gen_element_random(total=10, value_min=0, value_max=100):
    for i in range(total):
        yield randint(value_min, value_max)
        

# Преобразователь списка в виде функции
def more_previous(source_list):
    destin_list = []
    for i in range(1, len(source_list)):
        if source_list[i] > source_list[i - 1]:
            destin_list.append(source_list[i])
    return destin_list


print("A. Генератор в списковом ключении (list comprehension) для создания исходного массива и преобразование ввиде функций:")
source_lst_gen = gen_element_random(10)
source_lst = [i for i in source_lst_gen]
destin_lst = more_previous(source_lst)
print(f"in: {source_lst}")
print(f"to: {destin_lst}")

print("Б. Генератор в list comprehension для создания исходного массива и формирование выходного массива так же list comprehension:")
source_lst_gen = gen_element_random(10)
source_lst = [i for i in source_lst_gen]
destin_lst = [source_lst[i] for i in range(1, len(source_lst)) if source_lst[i] > source_lst[i - 1]]
print(f"in: {source_lst}")
print(f"to: {destin_lst}")

print("B. Потоковая обработка: генерируем данные и тут же не лету обрабатываем:")
source_lst = []  # инициализируем переменную для хранения исходного массива
destin_lst = []  # и результирующего
source_lst_gen = gen_element_random(10)  # инициализируем копию генератора, по которому будем итерировать
value_previous = next(source_lst_gen)    # первое значение
source_lst.append(value_previous)        # заносим его в исходный список
for value in source_lst_gen:
    source_lst.append(value)
    if value > value_previous:
        destin_lst.append(value) # если
    # готовимся к следующей итерации:
    # запоминаем пройденный элемент как предыдущий для следующей итерации
    value_previous = value
print(f"in: {source_lst}")
print(f"to: {destin_lst}")


print("End")

