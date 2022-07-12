# GeekBrains > Python basics: Oleg Gladkiy (https://geekbrains.ru/users/3837199)
homework_type = "Lesson-2. 4-Word"
# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
#    Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
#    Если в слово длинное, выводить только первые 10 букв в слове.

print(homework_type)


word_string = input("Input string: ")
word_list = word_string.split(" ")

for i in range(len(word_list)):
    word_number = i + 1
    print(f"{word_number:3d}  {(str(word_list[i]))[0:10]}")
    # f-строка не выполняет ограничение на 10 символом почему-то...
    #  print(f"{word_number:3d}  {str(word_list[i]):10}")

print(f"\nEnd")