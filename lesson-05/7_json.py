# GeekBrains, Python basics: Oleg Gladkiy (https://geekbrains.ru/users/3837199)
homework_type = "Lesson-5. 7-json: сериализация списка словарей"
''' Задание №:
7.  Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: 
    название, форма собственности, выручка, издержки.
    Пример строки файла: firm_1 ООО 10000 5000.
    Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
    Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
    
    Пример списка: 
        [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
        
    Итоговый список сохранить в виде json-объекта в соответствующий файл.
    Пример json-объекта:
        [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}] '''
print("\n" + homework_type + "\n")

import sys, os


filename = os.path.basename(sys.argv[0])     # имя этого модуля без маршрута
filename = filename.split('.')               # выделяем расширение
filename = "_".join(filename[:-1:])          # оставляем имя файла
data_file_in  = filename + "__FIRM_handmade.txt"
data_file_out = filename + "__FIRM_PROGmade.json"


def clear_string(s: str = ""):
    ''' Чистим строки от служебных непечатных символов '''
    chars = []
    for char in s:
        if char.isprintable():
            chars.append(char)
        elif char.isspace():     # Виды пробелов: b' \t\n\r\x0b\f'
            chars.append(" ")
        pass
    s = "".join(chars)
    if s.isspace():              # Проверка на пустую строку
        s = None
    return s


# Фирмы: получаем список

firms = []
with open(data_file_in, "r", encoding="utf-8") as file_in:
    firm_info = {}
    for string in file_in:
        if not (string := clear_string(string)):  # Подготовка строки...
            continue

        # Название фирмы

        words = string.split()
        name = []
        for index, word in enumerate(words, start=0):
            if not word.isdigit():
                name.append(word)
            else:
                break
        name = " ".join(name[:index - 1])

        # Финансовые показатели

        money = []
        for word in words[index-1::]:
            if word.isdigit():
                money.append(int(word))

        # firm_info[name] = []
        # firm_info[name].extend(money)
        firm_info[name] = money[0] - money[1]

firms.append(firm_info)

# Вычисляем

i = 0
profit_sum = 0
for key, profit in firms[0].items():
    if profit >= 0:
        i += 1
        profit_sum += profit
else:
    profit_average = profit_sum / i

firm_analytics = {}
firm_analytics['profit_average'] = profit_average
firms.append(firm_analytics)

# РЕЗУЛЬТАТ

print(firms)
