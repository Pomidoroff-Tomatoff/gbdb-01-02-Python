# GeekBrains > Python basics: Oleg Gladkiy (https://geekbrains.ru/users/3837199)
homework_type = "Lesson-3. 5_Sum"
# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
#    При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
#    разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться
#    к уже подсчитанной сумме. Но если вместо числа вводится специальный символ,
#    выполнение программы завершается. Если специальный символ введен после нескольких чисел,
#    то вначале нужно добавить сумму этих чисел к полученной ранее сумме
#    и после этого завершить программу.

# Прим.: работает с ошибкой, если после последней цифры введён пробел.

print(homework_type)

global nabor_sum, index_stop


def my_func_sum(input_string):
    nabor_list = input_string.split(' ')
    global index_stop, nabor_sum
    for el in nabor_list:
        if el == 'E' or el == 'e' or el == "У" or el == "у":
            index_stop = 1
        elif el == "":
            pass
        else:
            if el.isdigit():
                nabor_sum = nabor_sum + float(el)
    return

nabor_sum = 0
index_stop = 0
print("Ведите числа через пробел, завершение ввода -- символ 'E' (en))")
print("не вводите за последней цифрой в строке пробел")
while index_stop == 0:
    input_string = input("Ведите числа: ")
    my_func_sum(input_string)
    print(f"СУММА: {nabor_sum}")


print("End")
