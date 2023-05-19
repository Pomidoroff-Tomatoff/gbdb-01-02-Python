# GeekBrains > Python basics: Oleg Gladkiy (https://geekbrains.ru/users/3837199)
homework_type = "Lesson-8. 2_zero_division"
'''
  2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
     Проверьте его работу на данных, вводимых пользователем. 
     При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию 
     и не завершиться с ошибкой.
     РЕШЕНИЕ
        Заменить встроенное исключения я не могу (может это и хорошо),
        но зато могу подменить...
'''
print(homework_type)


class ApplicationZeroDivisionError(Exception):
    ''' Прикладной класс-исключение для обработки ошибки деления на ноль
        Внимание!
        1. При попытке деления на ноль данное исключение НЕ БУДЕТ вызвано
           по умолчанию (автоматически) как встроенное
        2. Автоматически вызывается ВСТРОЕННОЕ исключение ZeroDivisionError
        3. Для вызова этого прикладного исключения необходимо
           по месту отслеживания встроенного исключения ZeroDivisionError
           в качестве реакции определить вызов данного прикладного исключения
           инструкцией raise ApplicationZeroDivisionError(...)
    '''

    def __init__(self, message: str = ""):
        self.message = f"деление на ноль / {message}"

    def __str__(self):
        ''' Сообщение прикладного исключения '''
        return f"Неверно задан делитель, результат вычислить не получиться: {self.message}"


def get_value(message: str = ""):
    string = input(message)
    if string and not string.isspace():
        return float(string)


# Поехали
print("Введите числа или просто Enter для завершения")
while True:
    try:
        if (a := get_value("  введите числитель: ")) is None: break
        if (b := get_value("  введите делитель:  ")) is None: break

        try:
            y = a / b
        except ZeroDivisionError as errmsg:
            # Подменяем встроенное исключение на наше прикладное, а так же:
            # * подавляем встроенную цепочку трассировки
            # * используем встроенное сообщение, передавая его
            #   как аргумент прикладному экземпляру исключения.
            raise ApplicationZeroDivisionError(errmsg) from None

    except ApplicationZeroDivisionError as appmsg:
        print(appmsg)
    except Exception as err:
        print(f"неизвестная ошибка: {err}")
    else:
        print(f"Результат деления: {y}")


print("End")
