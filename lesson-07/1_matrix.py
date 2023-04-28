# GeekBrains > Python basics: Oleg Gladkiy (https://geekbrains.ru/users/3837199)
homework_type = "Lesson-7. 1-Matrix"
'''
# 1. Реализовать класс Matrix (матрица).
#    1.1 Обеспечить перегрузку конструктора класса (метод __init__()),
#        который должен принимать данные (список списков) для формирования матрицы.
#    Подсказка: 
#        матрица — система некоторых математических величин, 
#        расположенных в виде прямоугольной схемы.
#    Примеры матриц:
#       3 × 2:            3 × 3                 2 × 4
#      --------        -----------         --------------
#       31	22          3	5	32          3	5	8	3
#       37	43          2	4	 6          8	3	7	1
#       51	86         -1  64	-8
#
#    1.2 Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
#    1.3 Далее реализовать перегрузку метода __add__() для реализации операции сложения
#        двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
#        Подсказка:
#           сложение элементов матриц выполнять поэлементно —
#           1-ый элемент   1-ой строки первой матрицы складываем
#         с 1-ым элементом 1-ой строки второй матрицы и т.д. '''
print(homework_type)

import copy, time


class Matrix:
    ''' Матрица из целых цисел '''

    def __init__(self, matrix: list = []):
        self.__dim = self.__calculate_dimensions(matrix)
        self.__matrix = copy.deepcopy(matrix)

    def __calculate_dimensions(self, matrix):
        ''' вычисляем размерность данных матрицы '''
        d1 = len(matrix)      # строки
        d2 = len(matrix[0])   # столбцы
        dims = [d1, d2]
        return dims

    def get_dim(self):        # интерфейс
        return self.__dim

    def __str__(self):
        '''
        Магический метод: печатаем матрицу в привычном виде
        -- Преобразуем все числа в строки и складываем их в одну большую строку
        -- Находим самое длинное число, чтобы определить размер позиции для чисел
        '''

        def max_value_len():
            ''' Определяем максимальную длину числа в матрице '''
            max_values = [max(i, key=abs) for i in self.__matrix]  # ищем максимальные значения в списках
            max_value = abs(max(max_values, key=abs))  # самое большое по модулю
            word_precision = len(str(max_value)) + 1  # с учётом знака
            return word_precision

        words = []
        word_distance  = 1
        word_precision = max_value_len()
        for line in range(self.__dim[0]):
            for column in range(self.__dim[1]):
                words.extend(f"{self.__matrix[line][column]:>{word_precision}d}" + " "*word_distance)
            words.extend(f"\n")
        return "".join(words)  # возвращаем матрицу как большую строку с переводами каретки

    def __getitem__(self, item):
        return self.__matrix[item]

    def __add__(self, y_matrix):
        ''' Сложение двух матриц, перегрузка метода '''
        if not isinstance(y_matrix, self.__class__):
            raise ValueError(f"Матрицы должны быть одного типа {self.__class__}")

        # y_matrix_dim =
        if y_matrix.get_dim() != self.__dim:
            raise ValueError("Матрицы должны быть одинаковой размерности")

        sum_matrix = []                 # список для новой пустой матрицы
        for line in range(self.__dim[0]):
            sum_matrix.append([])       # добавляем пустую строку
            for column in range(self.__dim[1]):
                sum_matrix[line].append(self.__matrix[line][column] + y_matrix[line][column])

        return self.__class__(sum_matrix)
        # return self.this_class()(sum_matrix)  # можно и так вернуть новый экземпляр

    def __iadd__(self, y_matrix):
        ''' добавление к исходной другой матрицы '''
        # Проверка типа
        if not isinstance(y_matrix, self.__class__):
            raise ValueError(f"Матрицы должны быть одного типа {self.__class__}")
        # Проверка размерности
        if y_matrix.get_dim() != self.__dim:
            raise ValueError("Матрицы должны быть одинаковой размерности")

        for line in range(self.__dim[0]):
            for column in range(self.__dim[1]):
                self.__matrix[line][column] += y_matrix[line][column]

        return self

    @classmethod
    def this_class(cls):
        return cls

    pass  # class Matrix


# Поехали!
# Проверим работу класса на его экземплярах

l1 = [[1, 2, 3], [11, 12, -15], [21, 22, -25]]
l2 = [[1, 2, 3], [11, 12, -15], [21, 22, -25]]

m1 = Matrix(l1)
print("Исходная квадратная матрица 1:")
print(m1)
m2 = Matrix(l2)
print("Исходная квадратная матрица 2:\n" + str(m2))
print("Сложение исходных квадратных матриц 1 и 2:\n" + str(m1 + m2))

m1 += m2
print("Исходная квадратная матрица 1 после добавления к ней матрицы 2:\n" + str(m1))

print("Сложение матриц 5 на 2:\n",
    Matrix([[1, 2], [11, -12], [21, 22], [31, 32], [41, 42]]) +
    Matrix([[1, 2], [11, -12], [21, 22], [31, 32], [41, 42]])
)

print("Сложение матриц 2 на 5:\n" +
    str(
        Matrix([[1, 2, 3, 4, 5], [11, -12, 13, 14, 15]]) +
        Matrix([[1, 2, 3, 4, 5], [11, -12, 13, 14, 15]])
    )
)


print("End")
