# GeekBrains > Python basics: Oleg Gladkiy (https://geekbrains.ru/users/3837199)
homework_type = "Lesson-2. 3-Seasons"
# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
#    Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
#    Напишите решения через list и через dict.

print(homework_type)

season_list = ['winter', 'winter',            # 0, 1,
               'spring', 'spring', 'spring',  # 2, 3, 4,
               'summer', 'summer', 'summer',  # 5, 6, 7,
               'autumn', 'autumn', 'autumn',  # 8, 9, 10,
               'winter']                      # 11

season_dict = {'winter': [1, 2, 12],
               'spring': [3, 4, 5],
               'summer': [6, 7, 8],
               'autumn': [9, 10, 11]}

month_number = int(input("Введине номер месяца: "))

if (month_number >= 1) and (month_number <= 12):
    print(f"This is month of {(season_list[month_number - 1]).title()} (list)")

    # Решение со словарём перспективное, но моя реализация громоздка

    exit_code = 0
    for key_season in season_dict.keys():
        for value_month in season_dict[key_season]:
            if value_month == month_number:
                print(f"This is month of {key_season.upper()} (dictionary)")
                exit_code = 1
                break
        if exit_code == 1:
            break
else:
    print(f"Input error: value must be in range from  1 to 12.")

print(f"\nEnd")