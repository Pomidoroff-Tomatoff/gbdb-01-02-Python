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


class Singleton:
    ''' Классический (?) Singleton -- муть какая-то, но интересная '''
    def __new__(cls, *args, **kwargs):
        ''' * создаём Экземпляр, если он первый;
            * создаём Атрибут класса с адресом этого экземпляра,
              чтобы при последующих обращениях возвращать адрес этого экземпляра,
              вместо создания нового.
            * cls.instance: адрес единственного экземпляра
        '''
        if not hasattr(cls, 'instance'):            # ? -- атрибут класса для ссылки на экземпляр
            cls.instance = super().__new__(cls)     # Экземпляр! ...аргументы экз. не передаём...
        return cls.instance                         # Возвращаем ссылку на экз. всегда

class Date(Singleton):
    ''' Принимаем дату в виде строки формата «день-месяц-год»
        и конвертируем в цифровые значения даты
        __date_digits: собираем элементы даты
        __error_messages: собираем ошибки
    '''
    __date_digits = []
    __error_messages = []

    def __init__(self, sdate: str = ""):
        ''' Преобразованием входящую строку в цифровые данные
            и записываем их в переменную класса __date_digits
        '''
        self.__make_digital(sdate)

    @classmethod
    def __make_digital(cls, sdate):
        ''' Извлечение числовых данные из строки формата DD-MM-YYYY '''
        cls.__error_messages = []  # self.__class__.__error_messages = []  # это в некласных методах
        ddate = []
        status = True
        elements = [i for i in sdate.strip().split("-") if i and not i.isspace()]  # ...без пустышек
        for i in elements:
            try:
                value = int(i)
            except Exception as err:
                cls.__error_messages.append(f"Ошибка преобразования в целое: {err}.")
                status = False
            else:
                ddate.append(value)  # собираем элементы даты в список

        if status:  # Ошибки были?
            validate_error_messages = cls.__validate_digital(ddate)
            if validate_error_messages:
                cls.__error_messages.extend(validate_error_messages)
                status = False
            else:
                cls.__date_digits = ddate

        return status

    @staticmethod
    def __validate_digital(ddate: list =[]):
        ''' проверка компонентов даты '''
        error_messages = []
        rcode = True
        if len(ddate) < 3:
            print(f"Ошибка: нет данных")
            rcode = False
        else:
            if (day := ddate[0]) < 1 or day > 31:
                error_messages.append(f"Ошибка валидации: день = {day} не входит в допустимый диапазон")
                # print(f"Ошибка: день {day=} не входит в допустимый диапазон")
                rcode = False
            if (mon := ddate[1]) < 1 or mon > 12:
                error_messages.append(f"Ошибка валидации: месяц = {mon} не входит в допустимый диапазон")
                # print(f"Ошибка: месяц {mon=} не входит в допустимый диапазон")
                rcode = False
            if (year := ddate[2]) < 1900:
                error_messages.append(f"Ошибка валидации: год = {year} не входит в допустимый диапазон")
                # print(f"Ошибка: год {year=} не входит в допустимый диапазон")
                rcode = False
        return error_messages

    @classmethod
    def get_date_digits(cls):
        return cls.__date_digits

    @classmethod
    def get_err_msg(cls):
        return cls.__error_messages

    def __str__(self):
        ''' ...Усложняем, чтобы без ошибки вывести пустой список '''
        s = [f"{i:02d}" for i in self.get_date_digits()]
        s = "-".join(s) if len(s) > 0 else ""
        return s
    pass  # Date end


# Поехали


def main():
    """ ПРОВЕРКИ (тестирование класса Date)"""

    # константы для удобства
    DATE_STRING = "date_string"
    TEST_PLAN = "test_plan"
    ERROR_MSG = "error_message"
    INSTANCE = None

    tests = [
        {
            DATE_STRING: "1S-O5-202З",
            TEST_PLAN: "ОШИБКИ СИМВОЛЬНЫЕ: буквы вместо цифр 5--\"S\", 0--\"O\", 3--\"З\" (преобразование в целое)",
            INSTANCE: None,
            ERROR_MSG: None,
        }, {
            DATE_STRING: "32-01-2000",
            TEST_PLAN: "ОШИБКИ ДИАПАЗОНА: число дня месяца (__validate_digital)",
            INSTANCE: None,
            ERROR_MSG: None,
        }, {
            DATE_STRING: "23-23-2023",
            TEST_PLAN: "ОШИБКИ ДИАПАЗОНА: месяц (__validate_digital)",
            INSTANCE: None,
            ERROR_MSG: None,
        }, {
            DATE_STRING: "00-00-0000",
            TEST_PLAN: "ОШИБКИ ДИАПАЗОНА: число месяца, месяц и год (__validate_digital)",
            INSTANCE: None,
            ERROR_MSG: None,
        }, {
            DATE_STRING: "10-10-1000",
            TEST_PLAN: "ОШИБКИ ДИАПАЗОНА: год (__validate_digital)",
            INSTANCE: None,
            ERROR_MSG: None,
        }, {
            DATE_STRING: "10--01-  -2020",
            TEST_PLAN: "ОШИБКИ ФОРМАТА: лишние дефис и пробел (__make_digital)",
            INSTANCE: None,
            ERROR_MSG: None,
        }, {
            DATE_STRING: "18-05-2023",
            TEST_PLAN: "ТЕКУЩАЯ ДАТА (без ошибок)",
            INSTANCE: None,
            ERROR_MSG: None,
        }
    ]  # end tests

    print(f"\nCREATE INSTANCE of class Date & TEST\n")
    for i, test in enumerate(tests, start=1):
        test[INSTANCE] = instance = Date(test[DATE_STRING])
        test[ERROR_MSG] = instance.get_err_msg()
        print(f"{i:03d}-Test: {test[TEST_PLAN]}\n"
              f"      in: \'{test[DATE_STRING]}\'")
        for err in test[ERROR_MSG]:
            print(
              f"   ERROR: {err}")
        print(f"     out: \'{str(instance)}\' \n"
              f"list out: {instance.get_date_digits()} \n"
              f"instance: id={id(instance)} \n"
              )

    print(f"INSTANCE LIST FROM TEST\n")
    for i, test in enumerate(tests, start=1):
        print(f"{i:0>2d}-address: {test[INSTANCE]=}, id = {id(test[INSTANCE])}\n"
              f"      date: {test[INSTANCE]}"
              )


if __name__ == "__main__":
    main()
    print("End")
