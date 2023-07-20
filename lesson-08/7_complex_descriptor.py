# GeekBrains > Python basics: Oleg Gladkiy (https://geekbrains.ru/users/3837199)
homework_type = "Lesson-8. 7_complex_numbers v.028"
'''
  7. Реализовать проект «Операции с комплексными числами». 
     А. Создайте класс «Комплексное число». 
     Б. Реализуйте перегрузку методов сложения и умножения комплексных чисел. 
     В. Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа), 
        выполните сложение и умножение созданных экземпляров. 
        Проверьте корректность полученного результата.
        
     РЕШЕНИЕ
        -- Реальная и мнимая часть: свойства-дескрипторы класса re и im соответственно
        -- Дескриптор реализован как универсальный класс-дескриптор и может использоваться
           как для мнимой, так и для реальной частей -- указывается при инициализации... 
        -- Проверки типа чисел при создании и изменении реальной 
           и мнимой части комплексного числа: класс-декоратор CheckDigital -- контролируется в дескрипторе,
           что позволяет проверят из любого места программы 
        -- сложение и умножение: прикладные методы,  
           используемые в магических методах __add__() и так далее...
        -- Ошибки: классы прикладных исключений для контроля ошибок
        -- Сервис: методы представления и копирования объекта, запрещение создания посторонних атрибутов
     ПЛАН
        -- Использование приватных атрибутов, вместо обычных: ВЫПОЛНЕНО
        -- Использование дескрипторов для контроля изменения атрибутов: ВЫПОЛНЕНО
        -- Использование декораторов для проверок изменения значений: ВЫПОЛНЕНО
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


class AppAttribDeleteError(Exception):
    ''' Прикладное ИСКЛЮЧЕНИЕ: ошибка удаления атрибута '''

    def __init__(self, message: str = ""):
        self.message = f"{message}"

    def __str__(self):
        return f"Ошибка, атрибут удалить нельзя! {self.message}"


class ServiceComplex(object):
    '''Сервисные функции'''
    @staticmethod
    def get_args_value(*args, **kwargs):
        '''Получим последний аргумент value из множеств аргументов'''
        value = None
        if len(kwargs) == 0:  # все аргументы позиционные
            value = args[-1]
        else:
            if hasattr(kwargs, 'value'):
                value = kwargs['value']
            else:
                raise ValueError("Не задан аргумент для проверки")
        return value

    @staticmethod
    def set_args_value(value, /, *args, **kwargs):
        if len(kwargs) == 0:  # все аргументы позиционные
            args = list(args)
            args[-1] = value
            args = tuple(args)
        elif hasattr(kwargs, 'value'):
            kwargs['value'] = value
        else:
            raise ValueError("Не задан аргумент для проверки")
        return args, kwargs

    @staticmethod
    def is_number(value):
        if type(value) in (int, float):
            return True
        else:
            raise AppNumberError(f"недопустимый тип {type(value)} полученного значения \'{value}\'") from None


class CheckDigital(object):

    def __init__(self, num: int = 0):
        self.__num = num    # не используется...

    def __call__(self, f):
        def wrapper(*args, **kwargs):
            '''Проверка числа'''
            value = ServiceComplex.get_args_value(*args, **kwargs)
            if ServiceComplex.is_number(value):
                return f(*args, **kwargs)
            else:
                raise AppNumberError(value)
        return wrapper


class CheckComplex(object):
    '''Проверка принадлежности объекта к прикладному типу "комплексное число"'''
    def __init__(self, num: int = 0):
        self.__num = num    # не используется...

    def __call__(self, f):
        def wrapper(*args, **kwargs):
            value = ServiceComplex.get_args_value(*args, **kwargs)
            if not isinstance(value, ComplexNumber):  # object. или ComplexNumber.
                if ServiceComplex.is_number(value):
                    # Конвертируем реальное число в комплексное
                    # с нулевой мнимой частью! :-)
                    value = ComplexNumber(value, 0)
                    args, kwargs = ServiceComplex.set_args_value(value, *args, **kwargs)
                else:
                    raise AppNumberError(value)

            return f(*args, **kwargs)

        return wrapper


class NumberDESCRIPTOR(object):
    '''Дескриптор для работы с реальной и мнимой частями комплексного числа:
    один класс-дескриптор используется для создания нескольких свойств одного комплексного числа.
    Для того, чтобы эти свойства могли хранить свои значения, необходимо далее в экземплярах комплексных чисел
    создать атрибуты с именами, строго соответствующие своим свойствам.
    Например:
        re = NumberDESCRIPTOR()
            свойство re -> атрибут с именем _NumberDESCRIPTOR__re
    '''

    def __init__(self, doc: str = ""):
        # Запомним строку-описание свойства (или атрибута-дескриптора)
        self.__doc = doc

    def __set_name__(self, owner, name) -> None:
        '''Получение имени свойства, к которому привязан экз. дескриптора.
        Позволяет сформировать имя (атрибута), которое будет использовано для хранения значения своего свойства.
        Такое уникальное имя можно собрать, дополнив его именем его же свойства:
        Это собранное ИМЯ будем хранить здесь же -- в экземпляре дескриптора (исп. self).
            :param owner:  класс-владелец дескриптора;
            :param name:   имя свойства (атрибута), к которому привязан экземпляр класса-дескриптора.
        '''
        self.__attribute_name_for_descriptor = \
            "_" + self.__class__.__name__ + ("" if name.startswith("__") else "__") + name

    def __get__(self, instance, owner):
        '''Получение значения, сохранённого в экземпляре класса-владельца.
        Инициализация: первое значение экземпляр дескриптора получает в конструкторе экземпляра-владельца
            :param  self:      экземпляр этого дескриптора
            :param  instance:  экземпляр класса комплексного числа
            :param  owner:     класс комплексных чисел
        '''
        return instance.__dict__[self.__attribute_name_for_descriptor]

    @CheckDigital()
    def __set__(self, instance, value):
        '''Изменение значения атрибута-дескриптора,
        в том числе инициализация при первом обращении к экземпляру дескриптора
        в конструкторе экземпляра-владельца
            :param self:     экземпляр этого дескриптора
            :param instance: экземпляр класса комплексного числа
            :param value:    новое значение
        '''
        instance.__dict__[self.__attribute_name_for_descriptor] = value

    def __delete__(self, instance):
        raise AppAttribDeleteError(f"Атрибут \"{self.__attribute_name_for_descriptor}\". Дескриптор-класс \"{self.__class__.__name__}\".") from None


class ComplexNumber(object):
    '''Комплексное число'''

    re = NumberDESCRIPTOR('реальная')   # Экземпляр класса-дескриптора для свойства re, движок одинаков для всех свойств re во всех экз. ComplexNumber()
    im = NumberDESCRIPTOR('мнимая')     # Другой экз. дескр. NumberDESCRIPTOR -- для свойства im...

    def __init__(self, re: float = 0, im: float = 0):
        # Внимание!
        # Приватный атрибут дескриптора можно изменить только используя __dict__
        # с указанием класса, в котором он был создан: self.__dict__['_NumberDESCRIPTOR__real']
        # или (если принудительно имя класса не использовалось): self.__dict__['__real']
        # иначе он не видится...

        # Инициализируем дескрипторы для экземпляра
        self.re = re    # real, инициализация атрибута экземпляра дескриптора
        self.im = im    # imaginary, инициализация значения экземпляра дескриптора

    @CheckComplex()
    def __addition_begin(self, value):
        """Сложение комплексных экземпляров, проверка и корректировка -- декоратором"""
        re = self.re + value.re
        im = self.im + value.im
        return re, im

    def __add__(self, other):
        '''Сложение: я левый операнд:
           -- выполняем операцию и преобразуем результат сложения
              к комплексному типу (нашему прикладному)
           -- возвращаем новый экземпляр'''
        return ComplexNumber(*self.__addition_begin(other))

    def __radd__(self, other):
        '''Сложение: я правый операнд и срабатывает,
           когда левый операнд оказался реальным числом
           и не содержит метода __add__;
           возвращаем новый экземпляр'''
        return ComplexNumber(*self.__addition_begin(other))

    def __iadd__(self, other):
        '''Добавление ко мне новых данных,
           возвращаем себя же, а не новый экземпляр'''
        self.re, self.im = self.__addition_begin(other)
        return self

    # УМНОЖЕНИЕ

    @CheckComplex()
    def __multiplication_begin(self, value):
        """ Умножение, проверка и приведение типа -- декоратором"""
        re1 = self.re  # только для удобства,
        im1 = self.im  # чтобы избежать
        re2 = value.re     # путаницы
        im2 = value.im
        # Formula = (re1 + im1) * (re2 + im2) = (re1*re2) + im1*re2 + re1*im2 + (-im1*im2)
        re = re1 * re2 - im1 * im2
        im = im1 * re2 + re1 * im2
        return re, im

    def __mul__(self, other):
        return ComplexNumber(*self.__multiplication_begin(other))

    def __rmul__(self, other):
        return ComplexNumber(*self.__multiplication_begin(other))

    def __imul__(self, other):
        self.re, self.im = self.__multiplication_begin(other)
        return self

    # Представление

    def __str__(self):
        return f"({self.re:-.0f} {self.im:+.0f}i)"

    def __repr__(self):
        return f"({self.re:-.0f} {self.im:+.0f}i)"

    # СЕРВИС
    # Сервис: Запрет создания других атрибутов комплексного числа

    def __setattr__(self, key, value):
        '''Допускаем создание только атрибутов-свойств, то есть дескрипторов.
           Ограничиваем использования всех остальных атрибутов!
           Внимание!
           Атрибуты экземпляра этого класса, созданные экз. дескриптора, сюда не попадают!!!'''
        if key == 're' or key == 'im':
            # Пропускаем только изменения для указанных атрибутов
            object.__setattr__(self, key, value)
        else:
            # Остальные -- игнорируем или не допускаем, что вызывает исключение AttributeError
            # Следовательно: мы не можем создавать или использовать
            # все другие атрибуты.
            raise AppAttribError(f"Неизвестный атрибут \'{key}\'.")

    # Сервис: Копирование

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
    print(f"z0 = ComplexNumber(im=-1) ->  {z0} -- {z0.re=},  {z0.im=},  {type(z0.re)=}")
    z0.re = 1
    print(f"z0.re = 1                 ->  {z0} -- изменение атрибута напрямую")
    z1 = ComplexNumber(2, -1)
    print(f"z1 = ComplexNumber(2, -1) ->  {z1}")
    z2 = ComplexNumber(3, 6)
    print(f"z2 = ComplexNumber(3, 6)  ->  {z2}")
    print(f"z1 = ComplexNumber(2, -1) ->  {z1} -- повторный вывод предыдущего объекта для проверки, что значение сохранилось как значение экземпляра (а не класса)...")

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
        print(f"   {z1.param = }")
    except Exception as err:
        print(f" ! {err}")


# Поехали
if __name__ == "__main__":
    main()
    print("End")
