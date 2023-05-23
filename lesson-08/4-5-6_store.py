# GeekBrains > Python basics: Oleg Gladkiy (https://geekbrains.ru/users/3837199)
homework_type = "Lesson-8. 4-5-6_store"
'''
    4. Начните работу над проектом «Склад оргтехники». 
        А.  Создайте класс, описывающий склад. 
        Б.  А также класс «Оргтехника», который будет базовым для классов-наследников.
            Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). 
            -- В базовом классе определите параметры, общие для приведённых типов. 
            -- В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
     
    5.  Продолжить работу над первым заданием (п. 4). 
        Разработайте методы, которые отвечают за 
            > приём оргтехники на склад 
            > (и) передачу в определённое подразделение компании. 
        Для хранения данных о наименовании и количестве единиц оргтехники, 
        а также других данных, можно использовать любую подходящую структуру (например, словарь).
     
    6.  Продолжить работу над вторым заданием (п. 5). 
        Реализуйте механизм валидации вводимых пользователем данных.
         
        Например, 
            для указания количества принтеров, отправленных на склад, 
            нельзя использовать строковый тип данных.
     
    Подсказка: 
        постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, 
        изученных на уроках по ООП.
        
    РЕШЕНИЕ
        Идея: склад -- база данных оргтехники с ключевым полем по серийнику
              и функционал для работы с этой БД.
        
        > Вся оргтехника организуется как объекты-наследники 
          базового класса Equipment с характеристиками в виде словаря
          >> класс включает методы получения данных объекта
             * __call__ возвращает словарь данных объекта
             * __str__ возвращает отформатированную строку данных 
               для печати
          >> классы-наследники базового класса Equipment переопределяют
             атрибуты и методы родителя -- дополняя их.
               
        > Склад представляет из себя класс-синглтон:
          (мы это не проходили, но мне всё равно понравилось! :-) 
          >> размещающий у себя единый список объектов оборудования;
          >> ключевым полем всех объектов на складе является серийный номер
             * серийный номер не допускает дублирования
             * управления ошибкой дублирования введён класс исключений 
               AppDuplicateError(Exception)
             * ошибки с серийным номером управляется исключением 
               AppSerialError(Exception)
          >> методы операций с этим списком объектов: 
             * добавление (с валидацией только по серийнику, чтобы не раздувать код)
             * запрос всех объектов списком текстовых строк
             * запрос объекта оборудования по ключевому полю (серийник) 
             * изменение расположения -- изменение соотв. поля словаря
               с доступом к объекту по серийнику
               
        Примечание:
            1. Может быть корректнрее было бы организовать не склад, а базу активов оргтехники, 
               с возможным расположением "склад"?...
            2. Количество техники не подсчитывается...
'''
print(homework_type)
import abc


class Const:
    ''' Константы, только для удобства и минимизации скрытых ошибок констант '''
    NAME = 'name'
    SERIAL = 'serial'
    LOCATION = 'location'
    LOCATION_STORE = "store"
    LOCATION_RECEPTION = "reception"
    LOCATION_DEPARTMENT_SALE = "depart_sale"
    LOCATION_DEPARTMENT_LEGAL = "depart_legal"
    TYPE = 'type'
    TYPE_PRINTER = 'printer'
    TYPE_SCANNER = 'scanner'
    TYPE_COPIER = 'copier'
    PRINTER_DPI = 'resolution'           # разрешение принтера
    SCANNER_DMAX = 'dmax'                # оптическая плотность сканера
    COPIER_SPEED = 'copier_speed'        # скорость копирования образца


class Singleton:
    ''' Классический Singleton: возможен только один-единственный экземпляр,
        все остальные объекты -- ссылки на первоначальный объект
    '''
    def __new__(cls, *args, **kwargs):
        ''' * создаём Экземпляр, если он первый;
            * создаём Атрибут класса с адресом этого экземпляра,
              чтобы при последующих обращениях возвращать адрес этого экземпляра,
              вместо создания нового;
            * cls.instance: адрес единственного экземпляра
        '''
        if not hasattr(cls, 'instance'):            # ? -- атрибут класса для ссылки на экземпляр
            cls.instance = super().__new__(cls)     # Экземпляр! ...аргументы экз. не передаём...
        return cls.instance                         # Возвращаем ссылку на экз. всегда


class AppDuplicateError(Exception):
    ''' Прикладное исключение: дублирование ключевого значения '''

    def __init__(self, message: str = ""):
        self.message = f"ОШИБКА, дублирование ключевого значения: {message}"

    def __str__(self):
        return f"{self.message}"


class AppSerialError(Exception):
    ''' Прикладное исключение: не задан серийный номер '''

    def __init__(self, message: str = ""):
        self.message = f"ОШИБКА серийного номера: {message}"

    def __str__(self):
        return f"{self.message}"


class Equipment(abc.ABC):
    ''' Оргтехника -- базовый класс '''

    def __init__(self, equipment_type: str = "", serial: str = ""):
        if not serial or serial.isspace():
            raise AppSerialError("не задан")
        if not isinstance(serial, str):
            raise AppSerialError("тип не соответствует строковому")
        self.__item = {
            Const.TYPE: equipment_type,
            Const.NAME: None,
            Const.SERIAL: serial.upper(),
            Const.LOCATION: Const.LOCATION_STORE,
        }

    def _get_item(self):
        return self.__item

    def __call__(self):
        return self.__item

    @abc.abstractmethod
    def __str__(self):
        return (f"TYPE: {self.__item[Const.TYPE]:<10s}  " 
                f"NAME: {self.__item[Const.NAME]:<15s}  "
                f"SN: {self.__item[Const.SERIAL]:<15s}  "
                f"LOC: {self.__item[Const.LOCATION]:<13s}")  # .strip()


class Store(Singleton):
    ''' Склад, возможен только один уникальный экземпляр серийного номера '''

    __items = []  # список объектов оборудования

    @classmethod
    def set_item(cls, item: Equipment = None):
        ''' Приём техники на склад '''
        if cls.validation_serial(candidate=item):
            cls.__items.append(item)
            return True

    @classmethod
    def get_item(cls, serial: str = None):
        ''' Поиск оборудования по серийному номеру '''
        serial = serial.upper()
        for item in cls.__items:
            if item()[Const.SERIAL] == serial:
                return item
        return None

    @classmethod
    def set_location(cls, serial: str = "", location: str = None):
        ''' Определение размещения оборудования по серийнику '''
        if item := cls.get_item(serial=serial):
            item()[Const.LOCATION] = location
            return item()[Const.LOCATION]
        else:
            raise AppSerialError(f"{serial} не найден, изменение расположения отменено.")

    @classmethod
    def get_location(cls, serial: str = None):
        ''' Получить размещение оборудования '''
        return cls.get_item(serial=serial)()[Const.LOCATION]

    @classmethod
    def get_store_location(cls):
        ''' Все устройства на складе '''
        pass

    @classmethod
    def validation_serial(cls, candidate: Equipment = None):
        ''' Проверка серийного номера с имеющимися на складе '''
        if cls.get_item(candidate()[Const.SERIAL]) is not None:
            raise AppDuplicateError(
                f"такой серийный номер уже есть в базе\n"
                f"{candidate}")
        else:
            return True  # return и raise -- выходы из метода...

    @classmethod
    def __call__(cls, title: str = ""):
        ''' Список всего оборудования склада '''
        if title:                   # заголовок, если нужен
            print(title)
        for i, item in enumerate(cls.__items, start=1):
            print(f"{i:03d}  {item}")


class Printer(Equipment):
    ''' Тип оборудования: PRINTER '''

    def __init__(self, name: str = "", serial: str = "", dpi: int = 0):
        super().__init__(equipment_type=Const.TYPE_PRINTER, serial=serial)
        self.__item = self._get_item()        # получаем закрытый словарь родителя
        self.__item[Const.NAME] = name
        self.__item[Const.PRINTER_DPI] = dpi  # разрешение -- спец-парам. принтера

    def __str__(self):
        ''' Перегрузка родительского метода: добавляем DPI  '''
        return super().__str__() + f"  DPI: {self.__item[Const.PRINTER_DPI]:>4d}"


class Scanner(Equipment):
    ''' Тип оборудования: СКАНЕР '''

    def __init__(self, name: str = "", serial: str = "", dmax: float = 0):
        super().__init__(equipment_type=Const.TYPE_SCANNER, serial=serial)
        self.__item = self._get_item()          # получаем закрытый словарь родителя
        self.__item[Const.NAME] = name
        self.__item[Const.SCANNER_DMAX] = dmax  # разрешение -- спец-парам. принтера

    def __str__(self):
        ''' Перегрузка родительского метода: добавляем оптическую плотность '''
        return super().__str__() + f"  DMAX: {self.__item[Const.SCANNER_DMAX]:>3.1f}"


class Copier(Equipment):
    ''' Тип оборудования: КОПИРОВАЛЬНЫЙ АППАРАТ '''

    def __init__(self, name: str = "", serial: str = "", speed: int = 0):
        super().__init__(equipment_type=Const.TYPE_COPIER, serial=serial)
        self.__item = self._get_item()           # получаем закрытый словарь родителя
        self.__item[Const.NAME] = name
        self.__item[Const.COPIER_SPEED] = speed  # разрешение -- спец-парам. копира

    def __str__(self):
        ''' Перегрузка родительского метода: добавляем скорость копирования '''
        return super().__str__() + f"  SPEED: {self.__item[Const.COPIER_SPEED]:<4d}".rstrip()


def main():
    ''' Основной код модуля '''

    store = Store()            # инициализация склада

    p1 = Printer(name="Epson-MX", serial="001AFM27-40", dpi=300)  # создаём объекты
    p2 = Printer(name="Xerox-2415", serial="225KL-356", dpi=1200)
    s1 = Scanner(name="HP-2415-10", serial="18-25RY-10M", dmax=1.5)
    s2 = Scanner(name="Agfa-F4", serial="F4-4067KRX-8", dmax=2.0)
    c1 = Copier(name="Canon Office", serial="M4-0037PP18", speed=3)
    c2 = Copier(name="Canon Proff", serial="M3-0037PP19", speed=12)

    # Добавление оборудования на склад
    for item in [p1, p1, p2, s1, s2, c1, c2]:  # p1 пытаемся добавить 2-ды
        try:
            store.set_item(item=item)
        except Exception as err:
            print(f"{err}")
        else:
            print(f"Успешно добавлено: \n{item}")

    # Определяем размещение оборудования
    # проверяем
    print()
    print("Запрос устройства по серийному номеру 001AFM27-40:")
    print(store.get_item("001AFM27-40"))
    print(f"-- Расположение:      {store.get_location(serial='001AFM27-40')}")
    print(f"-- Новое размещение:  {store.set_location(serial='001AFM27-40', location=Const.LOCATION_RECEPTION)}")
    print(f"-- Распол. проверка:  {store.get_location(serial='001AFM27-40')}")
    print(p1)
    print("- "*46)
    print("Изменяем размещение оборудования: раздаём по отделам...")

    store.set_location(serial='M4-0037PP18', location=Const.LOCATION_DEPARTMENT_LEGAL)
    try:
        store.set_location(serial='M3-0037PP19---1', location=Const.LOCATION_DEPARTMENT_SALE)
    except Exception as err:
        print(err)
    store.set_location(serial='M3-0037PP19', location=Const.LOCATION_DEPARTMENT_SALE)
    store.set_location(serial='18-25RY-10M', location=Const.LOCATION_DEPARTMENT_SALE)

    print("- "*46)
    store("Склад, список всего оборудования компании:")


# Поехали
if __name__ == "__main__":
    main()
    print("End")
