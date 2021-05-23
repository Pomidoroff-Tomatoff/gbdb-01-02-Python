# GeekBrains > Python basics: Oleg Gladkiy (https://geekbrains.ru/users/3837199)
homework_type = "Lesson-3. 6_Title"
# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
#    но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
#    Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
#    Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
#    но каждое слово должно начинаться с заглавной буквы.
#    Необходимо использовать написанную ранее функцию int_func().

print(homework_type)


my_func_title = lambda input_string: input_string.title()
output_string = ""
print("Ведите строку из слов, разделённых пробелом")
print("Пустая строка -- завершение работы")

while True:
    input_string = input("Ваша строка: ")
    if input_string == "":
        break
    output_string = my_func_title(input_string)
    print(f"Результат:   {output_string}")


print("End")
