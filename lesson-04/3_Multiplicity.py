# GeekBrains > Python basics: Oleg Gladkiy (https://geekbrains.ru/users/3837199)
homework_type = "Lesson-4. 3-Multiplicity"
# 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
#    Подсказка: использовать функцию range() и генератор.

print(homework_type)

# source_number_list = [i for i in range(20, 241, 1)]
multiplicity_numbers = [i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0]

# print(source_number_list)
print(multiplicity_numbers)

print("End")
