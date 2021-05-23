# GeekBrains > Python basics: Oleg Gladkiy (https://geekbrains.ru/users/3837199)
homework_type = "Lesson-3. 2_NameArg"
# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
#    имя, фамилия, год рождения, город проживания, email, телефон.
#    Функция должна принимать параметры как именованные аргументы.
#    Реализовать вывод данных о пользователе одной строкой.

print(homework_type)


def u_profile(u_name="", u_surname="", u_year=0, u_city="", u_email="", u_tel=0):
    return str(u_name) + " " + str(u_surname) + " " + str(u_year) + " " + str(u_city) + " " + str(u_email) + " " + str(u_tel)

print(u_profile(u_name="Geek",
                u_tel="88007006841",   # Но телефон должен быть последним в выводе
                u_surname="Brains",
                u_year=2000,
                u_city="Moscow",
                u_email="support@geekbrains.ru"))


print("End")
