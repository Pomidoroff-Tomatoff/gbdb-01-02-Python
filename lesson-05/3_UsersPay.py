# GeekBrains > Python basics: Oleg Gladkiy (https://geekbrains.ru/users/3837199)
homework_type = "Lesson-5. 3_UsersPay"
# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
#    Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
#    Выполнить подсчет средней величины дохода сотрудников.

print(homework_type)


file_data_name = "3_UsersPay_DATA_handmade.txt"
pay_min = 20000


def special_symbol_remover(str):

    while str.find('\n') >= 0:
        str = str.replace('\n', '')   # спецсимвол передвода строки -- удаляем

    while str.find('  ') >= 0:
        str = str.replace('  ', ' ')  # все двойные пробелы заменяем на одинарные

    return str


worker_pay = 0
worker_pay_average = 0
with open(file_data_name, "r", encoding="utf-8") as file_data:
    print(f"Список сотрудников, с зарплатой менее {pay_min}:")
    worker_list_count = 0
    for str_in in file_data:
        str_in = special_symbol_remover(str_in)
        worker_record = str_in.split(' ')   # получаем список элементов для работника
        if len(worker_record) > 1:          # отсекаем работников без зарплаты
            if worker_record[1].isdigit():  # проверка
                worker_list_count += 1
                worker_pay_average = int(worker_record[1])
                if worker_pay_average < pay_min:
                    print(f"{worker_record[0]:<20} {worker_record[1]: >7}")

    worker_pay_average = int(worker_pay_average / worker_list_count)
    print(f"\nСредняя зарплата: {worker_pay_average}")


print("End")