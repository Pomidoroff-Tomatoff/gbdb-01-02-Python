# GeekBrains > Python basics: Oleg Gladkiy (https://geekbrains.ru/users/3837199)
homework_type = "Lesson-8. 7_complex_numbers v.017"
'''
  7. Реализовать проект «Операции с комплексными числами». 
     А. Создайте класс «Комплексное число». 
     Б. Реализуйте перегрузку методов сложения и умножения комплексных чисел. 
     В. Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа), 
        выполните сложение и умножение созданных экземпляров. 
        Проверьте корректность полученного результата.
        
     РЕШЕНИЕ
        -- Реальная и мнимая часть: атрибуты класса re и im соотв.
        -- Проверки типа чисел при создании и изменении реальной 
           и мнимой части комплексного числа: __setattr__(), 
           что позволяет контролировать изменение атрибутов из любой части программы.
        -- сложение и умножение: прикладные методы,  
           используемые в магических методах __add__() и так далее...
        -- Ошибки: классы прикладных исключений для контроля ошибок
        -- Сервис: методы представления и копирования объекта
     ПЛАН
        -- Использование приватных атрибутов, вместо обычных
        -- Использование дескрипторов для контроля изменения атрибутов...
        -- (уточнение имён прикладных методов...)
'''
print(homework_type)


class AppNumberError(Exception):
    ''' Прикладное ИСКЛЮЧЕНИЕ: введены буквы, а не цифры '''

    def __init__(self, message: str = ""):
        self.message = f"{message}"

    def __str__(self):
        return f"Ошибка числового значения: {self.message}"


class AppAttribError(Exception):
    ''' Прикладное ИСКЛЮЧЕНИЕ: недопустимый атрибут '''

    def __init__(self, message: str = ""):
        self.message = f"{message}"

    def __str__(self):
        return f"Ошибка, недопустимый атрибут. {self.message}"


class ComplexNumber(object):
    '''Комплексное число'''

    def __init__(self, re: float = 0, im: float = 0):
        self.re = re   # real
        self.im = im   # imaginary

    # Проверки и приведение типа, контроль присваивания значений

    @staticmethod
    def __is_number(value):
        if isinstance(value, (int, float)):
            return True

    def __complex_object(self, value):
        '''Проверка и приведение типа
           -- если получено реально число, то приводим его
              к комплексному с нулевой мнимой часть
           -- если приведение невозможно, то генерируем исключение'''
        if isinstance(value, type(self)):  # object. или ComplexNumber.
            # всё в порядке: тип комплексный
            return value
        else:
            # Конвертируем реальное число в комплексное
            # с нулевой мнимой частью! :-)
            return ComplexNumber(value, 0)

    def __getattribute__(self, item):
        '''Оставим, чтобы поэкспериментировать'''
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        '''Проверка типа реальной и мнимой частей,
           а так же ограничение использования всех остальных атрибутов'''
        if key == 're' or key == 'im':
            if not self.__is_number(value):
                raise AppNumberError(f"недопустимый тип {type(value)} полученного значения {value}") from None
            else:
                object.__setattr__(self, key, value)
        else:
            # Пропускаем только изменения для указанных атрибутов,
            # остальные -- игнорируем, что вызывает исключение AttributeError
            # Следовательно: мы не можем создавать или использовать
            # все другие атрибуты.
            raise AppAttribError(f"неизвестный атрибут {key}")

    # СЛОЖЕНИЕ

    def __addition_complex(self, value=None):
        """ Сложение с проверкой и приведением типа """
        z = self.__complex_object(value)
        re = self.re + z.re
        im = self.im + z.im
        return re, im

    def __add__(self, other):
        '''Сложение: я левый операнд:
           -- выполняем операцию и преобразуем результат сложения
              к комплексному типу (нашему прикладному)
           -- возвращаем новый экземпляр'''
        return ComplexNumber(*self.__addition_complex(other))

    def __radd__(self, other):
        '''Сложение: я правый операнд и срабатывает,
           когда левый операнд оказался реальным числом
           и не содержит метода __add__;
           возвращаем новый экземпляр'''
        return ComplexNumber(*self.__addition_complex(other))

    def __iadd__(self, other):
        '''Добавление ко мне новых данных,
           возвращаем себя же, а не новый экземпляр'''
        self.re, self.im = self.__addition_complex(other)
        return self

    # УМНОЖЕНИЕ

    def __multiplication_complex(self, value):
        """ Умножение с проверкой и приведением типов """
        z = self.__complex_object(value)
        re1 = self.re  # толь для удобства
        im1 = self.im  # чтобы избежать
        re2 = z.re     # путаницы
        im2 = z.im
        # Formula = (re1 + im1) * (re2 + im2) = (re1*re2) + im1*re2 + re1*im2 + (-im1*im2)
        re = re1 * re2 - im1 * im2
        im = im1 * re2 + re1 * im2
        return re, im 

    def __mul__(self, other):
        return ComplexNumber(*self.__multiplication_complex(other))

    def __rmul__(self, other):
        return ComplexNumber(*self.__multiplication_complex(other))

    def __imul__(self, other):
        self.re, self.im = self.__multiplication_complex(other)
        return self

    # Представление

    def __str__(self):
        return f"({self.re:-.0f} {self.im:+.0f}i)"

    def __repr__(self):
        return f"({self.re:-.0f} {self.im:+.0f}i)"

    # СЕРВИС: Копирование

    def copy(self):
        return ComplexNumber(self.re, self.im)

    def __copy__(self):
        return self.copy()

    def __deepcopy__(self):
        return self.copy()


def main():
    ''' Основной код программы '''

    # СОЗДАНИЕ комплексных чисел
    print(f"\nСОЗДАНИЕ объектов -- комплексных чисел")
    z0 = ComplexNumber(im=-1)
    print(f"z0 = ComplexNumber(im=-10)->  {z0}")
    z0.re = 1
    print(f"z0.re = 1                 ->  {z0} -- изменение атрибута напрямую")
    z1 = ComplexNumber(1, -1)
    print(f"z1 = ComplexNumber(2, -1) ->  {z1}")
    z2 = ComplexNumber(3, 6)
    print(f"z2 = ComplexNumber(3, 6)  ->  {z2}")

    # СЛОЖЕНИЕ

    print(f"\nСЛОЖЕНИЕ комплексных чисел")
    z3 = z1 + z2
    print(f"z3 = z1 + z2         ->  {z3 = }")
    z4 = 1000 + z3
    print(f"z4 = 1000 + z3       ->  {z4 = }")
    z3 += -5
    print(f"z3 += -5             ->  {z3 = }")
    z3 += 0
    print(f"z3 += 0              ->  {z3 = }")

    # УМНОЖЕНИЕ

    print(f"\nУМНОЖЕНИЕ комплексных чисел")
    z5 = z1 * z2
    print(f"z5 = z1 * z2  -> {z5 = }")
    z6 = z1 * 2
    print(f"z6 = z1 * 2   -> {z6 = }")
    z6 *= 0
    print(f"z6 *= 0       -> {z6 = }")

    # ОШИБКИ (тест отработки ошибок)

    print(f"\nОШИБКИ")
    print(f'-- Попытка выполнить операцию сложения со строкой')
    value_str = '-STRING-'
    try:
        print(f"   Операция: z1 += '{value_str}', результат:")
        z1 += value_str
    except Exception as err:
        print(f" ! {err}")
    finally:
        print(f"   Проверка: {z1 = } (ошибочные данные не внесены)")

    print(f'')
    print(f'-- Попытка создать комплексное число со строкой в реальной части')
    value_str = 'REAL-AS-STRING'
    try:
        print(f"   Операция: z_test = ComplexNumber('{value_str}', 0), результат:")
        z_test = None
        z_test = ComplexNumber(value_str, 0)
    except Exception as err:
        print(f" ! {err}")

    print(f'')
    print(f'-- Попытка изменить атрибут экземпляра на строку...')
    value_str = 'STRING-FOR-ATTRIBUTE'
    try:
        print(f"   Операция: z1.re = '{value_str}', результат:")
        z1.re = value_str
    except Exception as err:
        print(f" ! {err}")

    print(f'')
    print(f'-- Попытка создать новый атрибут...')
    try:
        print(f"   Операция: z1.param = 111, результат:")
        z1.param = 111
    except Exception as err:
        print(f" ! {err}")


# Поехали
if __name__ == "__main__":
    main()
    print("End")
