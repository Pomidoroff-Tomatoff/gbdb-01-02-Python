# GeekBrains > Python basics: Oleg Gladkiy (https://geekbrains.ru/users/3837199)
homework_type = "Lesson-3. 2_NameArg"
# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
#    имя, фамилия, год рождения, город проживания, email, телефон.
#    Функция должна принимать параметры как именованные аргументы.
#    Реализовать вывод данных о пользователе одной строкой.

print(homework_type)


def u_profile(**kwargs):
    user_str = ""
    for key, value in kwargs.items():
        user_str += str(value) + " "   # в конце строки тоже будет пробел...
    return user_str


print(u_profile(u_name="Geek",
                u_surname="Brains",
                u_year=2000,
                u_city="Moscow",
                u_email="support@geekbrains.ru",
                u_tel = "88007006841",  # Но телефон должен быть последним в выводе
                )
      )

print("End")
