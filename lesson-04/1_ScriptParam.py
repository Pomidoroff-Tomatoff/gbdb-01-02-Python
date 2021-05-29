# GeekBrains > Python basics: Oleg Gladkiy (https://geekbrains.ru/users/3837199)
homework_type = "Lesson-4. 1-ScriptParam"
# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
#    В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
#    Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

import sys
import os

arg_list = sys.argv
script_param__error_cmdline = dict(
    no_arg='Ошибка командной строки: параметры не заданы',
    too_many_arg='Слишком много аргументов',
    not_enough_arg='Недостаточно аргументов',
    bad_number='Все агрументы должны быть целыми положительными числами'
)


# Функция проверок параметров командной стоки
# Если что-то не так, то выводим сообщение о найденной ошибке
# и возвращаем код ошибки (для критичной он больше 10)
def script_usage_verify():
    global script_param__error_cmdline
    global arg_list
    script_name = os.path.basename(arg_list[0])
    error_index = 0

    def script_usage():
        print("Script Usage:")
        print(f"{script_name} Выработка Ставка Премия")
        print(f"-- Выработка: время, затраченное на выполнение работы (часы)\n"
              f"-- Ставка: оплата за 1 час (рубли)\n"
              f"-- Премия: дополнительная облата (рубли), необъязательный параметр")
        return

    if len(arg_list) == 1:
        error_index = 11
        print(script_param__error_cmdline.get('no_arg'))
        script_usage()
    elif len(arg_list) > 4:
        error_index = 11
        print(script_param__error_cmdline.get('too_many_arg'))
        script_usage()
    elif len(arg_list) < 3:
        error_index = 11
        print(script_param__error_cmdline.get('not_enough_arg'))
        script_usage()
    else:
        for index in range(1, len(arg_list)):
            if arg_list[index].isdigit():
                continue
            else:
                error_index = 13
                print(f"Ошибка! {script_param__error_cmdline.get('bad_number')}")
                break
    return error_index


# Функция вычислений с проверкой
def pay():
    try:
        work_time = int(arg_list[1])
        work_rate = int(arg_list[2])
        pay_sum = work_time * work_rate
        if len(arg_list) > 3:
            work_bonus = int(arg_list[3])
        else:
            work_bonus = 0
        pay_sum += work_bonus
    except:
        pay_sum = None
    return pay_sum


# Основная программа
if __name__ == "__main__":
    print(homework_type)
    if not script_usage_verify() > 10:
        print(f"Расчитанная оплата: {pay()}")
    else:
        exit(1)
