# GeekBrains > Python basics: Oleg Gladkiy (https://geekbrains.ru/users/3837199)
# Lesson-1. 2-Time
# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды.
#    Выведите в формате чч:мм:сс. Используйте форматирование строк.

homework_type = "Lesson-1. 2-Time"
print(homework_type)

seconds_in = {'day': (60 * 60 * 24), 'hour': (60 * 60), 'min': 60}


def time_in_day(i_sec_all):
    i_day = i_sec_all // seconds_in["day"]
    i_sec_rest = i_sec_all % seconds_in["day"]

    i_hour = i_sec_rest // seconds_in["hour"]
    i_sec_rest = i_sec_rest % seconds_in["hour"]

    i_min = i_sec_rest // seconds_in["min"]
    i_sec = i_sec_rest % seconds_in["min"]

    if i_day <= 0:
        print(f"Your entered time: {i_hour}:{i_min}:{i_sec}.")
    else:
        print(f"Your entered time: {i_hour}:{i_min}:{i_sec} and {i_day} day.")


i_seconds = 0
count = 1
count_max = 5
while count <= count_max:
    count += 1
    input_string = input("Enter the time in seconds: ")
    if not input_string.isalpha():
        try:
            i_seconds = int(input_string)
        except:
            print(f"WORNING! Value mast be integer digital. Repeat (iteration {count} of {count_max}...")
            continue

        if i_seconds < 0:
            print(f"WORNING! Value mast be positive. Repeat (iteration {count} of {count_max}...")
            continue
        else:
            print("")
            time_in_day(i_seconds)
            break
    else:
        print(f"WORNING! Value mast be digital. Repeat (iteration {count} of {count_max}...")
        continue

print("End of program")
