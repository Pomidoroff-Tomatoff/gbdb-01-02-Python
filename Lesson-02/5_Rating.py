# GeekBrains > Python basics: Oleg Gladkiy (https://geekbrains.ru/users/3837199)
homework_type = "Lesson-2. 5-Rating"
# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
#    У пользователя необходимо запрашивать новый элемент рейтинга.
#    Если в рейтинге существуют элементы с одинаковыми значениями,
#    то новый элемент с тем же значением должен разместиться после них.

rating_list = list()

print(homework_type)

while True:
    rating_in = input("Input rating value: ")
    if len(rating_in) == 0:
        break
    rating_in_digit = int(rating_in)
    rating_list.insert(1, rating_in_digit)
    rating_list.sort(reverse=True)
    print(f"{rating_in_digit:5d},  List: {rating_list}")

print(f"\nEnd")