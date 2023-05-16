# GeekBrains > Python basics: Oleg Gladkiy (https://geekbrains.ru/users/3837199)
homework_type = "Lesson-8. 1_date"
'''
# 1. Реализовать класс «Дата»
     А. функция-конструктор которого должна принимать дату в виде 
        строки в формате «день-месяц-год». 
     Б. В рамках класса реализовать два метода: 
        1-ый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать 
            их тип к типу «Число».
        2-ой, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года 
            (например, месяц — от 1 до 12).
     В. Проверить работу полученной структуры на реальных данных.
  РЕШЕНИЕ:
     А. Концепция
        Использование метода класса обосновано, если необходимо содержать дату 
        как переменную (атрибут) класса. В поставленной задаче это единственный требуемый
        атрибут. Следовательно, все экземпляры класса будут обращаться к одному атрибуту.
        Данный тип класса соответствует классу-синглтону -- Singlton может иметь
        только один экземпляр, хоть и под разными именами.
     Б. Создать класс сингл-тон для хранения и выдачи значения даты.
     В. Создать методы для разбора даты и обработки ошибок.
'''
print(homework_type)


class Date:
    ''' Принимаем дату в виде строки формата «день-месяц-год»
        и конвертируем в цифровые значения даты
        sdate: дата в виде строки
    '''

    __date_digits = []

    def __new__(cls, *args, **kwargs):
        ''' Классический экземпляр Singleton '''
        if not hasattr(cls, 'instance'):
            # создаём атрибут класса для ссылки на экземпляр
            # ...здесь в __new__ доп. аргументы НЕ указываются...
            cls.instance = super().__new__(cls)

        return cls.instance  # возвращаем ссылку на экз.

    def __init__(self, sdate: str = ""):
        self.__make_digital(sdate)

    @classmethod
    def __make_digital(cls, sdate):
        ''' извлечение числовых данные из строки
            формата dd-mm-yy '''
        try:
            ddate = [int(i) for i in sdate.strip().split("-") if i]  # исключаем пустые элементы
        except Exception as err:
            print(f"Ошибка преобразования в целые числа элементов даты \"{sdate}\".", err)
        else:
            if cls.__validate_digital(ddate):
                cls.__date_digits = ddate
        return cls.__date_digits

    @staticmethod
    def __validate_digital(ddate: list =[]):
        ''' проверка компонентов даты '''
        rcode = True
        if len(ddate) < 3:
            print(f"Ошибка: нет данных")
            rcode = False
        if ddate[0] > 31:
            print(f"Ошибка: день месяца {ddate[0]=}")
            rcode = False
        if ddate[1] > 12:
            print(f"Ошибка: месяц {ddate[1]=}")
            rcode = False
        if ddate[2] < 1900:
            print(f"Ошибка: год  {ddate[2]=}")
            rcode = False
        return rcode

    @classmethod
    def get_date_digits(cls):
        return cls.__date_digits

    def __str__(self):
        s = [f"{i:02d}" for i in self.get_date_digits()]
        s = "-".join(s) if len(s) > 0 else ""
        return s


# ПРОВЕРКИ

# Ошибки задания чисел даты -- буквы вместо цифр: "S", "O", "З"
print("\nОШИБКИ цифр:")
d1 = Date("1S-O5-202З")
print(f"{d1 = } -> {str(d1) = }, list = {d1.get_date_digits()}")

# Ошибка задания числа месяца:
d2 = Date("32-05-2023")
print(f"{d2 = } -> {str(d2) = }, list = {d2.get_date_digits()}")

# ВЕРНЫЕ значения
print("\nОШИБКИ формата; попытка создания разных объектов...")
d3 = Date("01--05-2018")
print(f"{d3 = } -> {str(d3) = }, list = {d3.get_date_digits()}")
print("Создаём d4 с новой датой, а изменения проверяем в d3:")
d4 = Date("21-03-2023")
print(f"{d4 = } <- {str(d4) = }, list = {d3.get_date_digits()}")

print("End")
