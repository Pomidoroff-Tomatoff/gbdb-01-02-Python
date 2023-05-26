# GeekBrains > Python basics: Oleg Gladkiy (https://geekbrains.ru/users/3837199)
homework_type = "Lesson-8. 4-5-6_store. v.020"
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
            1. Данные организованы в виде словаря в объекте единице оборудования, 
               а не отдельных атрибутов.
            2. Общая база данных размещена в классе-синглтоне Store в виде списка объектов оборудования, 
               со словарём параметров в каждом таком объекте.
            3. Для техники в качестве базового используется абстрактный класс.
            4. Валидация вручную; __setattr__ не используется -- не понятно, как это сделать для словаря.
            5. Может быть корректнее было бы организовать не склад, а базу активов оргтехники, 
               с возможным расположением "склад"?...
            6. Количество техники __len__ подсчитывается только общее -- без учёта выборки 
               (например, по расположению).
            7. Сложная получилась конструкция. Оценить её жизнеспособность сейчас так же сложно...
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
        ''' * создаём первый Экземпляр. Только если он первый;
            * создаём Атрибут класса с адресом этого 1-ого экземпляра,
              чтобы при последующих обращениях возвращать адрес этого экземпляра,
              вместо создания нового;
            * cls.instance: адрес единственного экземпляра
        '''
        if not hasattr(cls, 'instance'):            # ? -- атрибут класса для ссылки на экземпляр
            cls.instance = super().__new__(cls)     # Экземпляр! ...аргументы экз. не передаём...
        return cls.instance                         # Возвращаем ссылку на 1-ый экз. Всегда!


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


class AppEquipmentError(Exception):
    ''' Прикладное исключение: неверный тип объекта оборудования '''

    def __init__(self, message: str = ""):
        self.message = f"ОШИБКА класса (типа) -- объект не соответствует классу (типу) Equipment: {message}"

    def __str__(self):
        return f"{self.message}"


class AppValueError(Exception):
    ''' Прикладное исключение: неверное значение параметра оборудования '''

    def __init__(self, message: str = ""):
        self.message = f"ОШИБКА параметра оборудования: {message}"

    def __str__(self):
        return f"{self.message}"


class Equipment(abc.ABC):
    ''' Оргтехника -- базовый абстрактный класс,
        не может иметь собственных объектов-экземпляров
        (совместно с абстрактными методами этого абс. класса)
    '''

    def __init__(self, equipment_type: str = "", name: str = "", serial: str = ""):
        ''' Инициализируем атрибут(ы) экземпляра '''
        # Атрибут (приватный) экземпляра -- словарь данных...
        self.__item = {
            Const.TYPE: equipment_type,
            Const.NAME: self.valid_name(name),
            Const.SERIAL: self.valid_serial(serial),
            Const.LOCATION: Const.LOCATION_STORE,
        }

    @staticmethod
    def valid_name(s: str = ""):
        if not s and not s.isspace():
            AppValueError(f"Пустое значение")
        if not isinstance(s, str):
            AppValueError(f"Недопустимая строка, тип {type(s)}")
        s = s.strip()
        if len(s) > 20:
            AppValueError(f"Слишком длинное значение {len(s)}")
        return s

    @staticmethod
    def valid_serial(s: str = ""):
        if not s and not s.isspace():
            raise AppSerialError("не задан")
        if not isinstance(s, str):
            raise AppSerialError(f"тип не соответствует строковому {type(s)}")
        s = s.strip()
        if len(s) > 20:
            raise AppSerialError(f"Слишком длинное значение {len(s)}")
        return s.upper()

    def get_info(self):
        ''' Доступ к приватным атрибутам '''
        return self.__item

    @property
    def get_serial(self):
        ''' Доступ к серийнику '''
        return self.__item[Const.SERIAL]

    @property
    def get_location(self):
        ''' Доступ к размещению '''
        return self.__item[Const.LOCATION]

    def __call__(self):
        return self.__item

    @abc.abstractmethod
    def __str__(self):
        ''' Преобразование экземпляра в строку
            абстрактный метод: требует перегрузки у наследника
        '''
        return (f"TYPE: {self.__item[Const.TYPE]:<10s}  " 
                f"NAME: {self.__item[Const.NAME]:<15s}  "
                f"SN: {self.__item[Const.SERIAL]:<15s}  "
                f"LOC: {self.__item[Const.LOCATION]:<13s}")


class Store(Singleton):
    ''' Склад, возможен только один уникальный экземпляр серийного номера '''

    __items = []  # список объектов оборудования

    @classmethod
    def set_item(cls, item: Equipment = None):
        ''' Приём техники на склад '''
        if isinstance(item, Equipment):
            if cls.validation_serial(candidate=item):
                cls.__items.append(item)
                return True
        else:
            raise AppEquipmentError(type(item))

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
    def __call__(cls, location: str = ""):
        ''' Список оборудования по его размещению '''
        if location and not location.isspace() and location is not None:
            i = 0
            for item in cls.__items:
                if item.get_location == location:
                    i += 1
                    print(f"{i:03d}  {item}")
        else:
            for i, item in enumerate(cls.__items, start=1):
                print(f"{i:03d}  {item}")

    @classmethod
    def __iter__(cls):
        return iter(cls.__items)

    @classmethod
    def __len__(cls):
        return len(cls.__items)

    def __add__(self, other):
        self.set_item(item=other)
        return self

    def __radd__(self, other):
        self.set_item(item=other)
        return self

    def __iadd__(self, other):
        self.set_item(item=other)
        return self


class Printer(Equipment):
    ''' Тип оборудования: PRINTER '''

    def __init__(self, name: str = "", serial: str = "", dpi: int = 0):
        super().__init__(equipment_type=Const.TYPE_PRINTER, name=name, serial=serial)
        self.__item = self.get_info()         # получаем приватный словарь родителя
        self.__item[Const.PRINTER_DPI] = dpi  # печатное разрешение (спец-парам. принтера)

    def __str__(self):
        ''' Перегрузка родительского метода: добавляем DPI  '''
        return super().__str__() + f"  DPI: {self.__item[Const.PRINTER_DPI]:>4d}"


class Scanner(Equipment):
    ''' Тип оборудования: СКАНЕР '''

    def __init__(self, name: str = "", serial: str = "", dmax: float = 0):
        super().__init__(equipment_type=Const.TYPE_SCANNER, name=name, serial=serial)
        self.__item = self.get_info()           # получаем приватный словарь родителя
        self.__item[Const.SCANNER_DMAX] = dmax  # оптическая плотность (спец-парам.)

    def __str__(self):
        ''' Перегрузка родительского метода: добавляем оптическую плотность '''
        return super().__str__() + f"  DMAX: {self.__item[Const.SCANNER_DMAX]:>3.1f}"


class Copier(Equipment):
    ''' Тип оборудования: КОПИРОВАЛЬНЫЙ АППАРАТ '''

    def __init__(self, name: str = "", serial: str = "", speed: int = 0):
        super().__init__(equipment_type=Const.TYPE_COPIER, name=name, serial=serial)
        self.__item = self.get_info()            # получаем приватный словарь родителя
        self.__item[Const.COPIER_SPEED] = speed  # скорость (спец-парам. копира)

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
    c2 = Copier(name="Canon Pro", serial="M3-0037PP19", speed=12)

    # Добавление оборудования на склад
    # -- p1 пытаемся добавить дважды (ошибка ключевого поля SN)
    # -- пытаемся добавить строку вместо объекта оборудования (ошибка типа)
    print("- "*46)
    print("Добавление оборудования на склад")
    for item in [p1, p1, p2, s1, s2, c1, c2, "ошибочно задан неверный тип объекта"]:
        try:
            # store.set_item(item=item)     # можно и так
            # store += item                 # можно и так
            # store = store + item          # можно и так
            store = item + store
        except Exception as err:
            print(f"{err}")
        else:
            print(f"Успешно добавлено: \n{store.get_item(serial=item.get_serial)}")
    print("- "*46)
    print("Удаление переменные-ссылки на объекты: ")
    print("но проверим, остались ли объекты на складе после удаления переменны?")
    del p1, p2, s1, s2, c1, c2
    try:
        print(p1)  # попытка обратиться к удалённой переменной
    except Exception as err:
        print(f"ПЕРЕМЕННАЯ p1 УДАЛЕНА: {err}")

    # Изменение расположения

    print("- "*46)
    print("Изменяем размещение оборудования: раздаём по отделам...")

    store.set_location(serial='M4-0037PP18', location=Const.LOCATION_DEPARTMENT_LEGAL)
    try:
        print("Попытка изменить размещение объекта с неверным SN: M3-0037PP19---1")
        store.set_location(serial='M3-0037PP19---1', location=Const.LOCATION_DEPARTMENT_SALE)
    except Exception as err:
        print(err)
    store.set_location(serial='M3-0037PP19', location=Const.LOCATION_DEPARTMENT_SALE)
    store.set_location(serial='18-25RY-10M', location=Const.LOCATION_DEPARTMENT_SALE)

    print("- "*46)
    print(f"Склад, список всего оборудования компании (проверяем новое размещение)")
    store()
    print(f"ВСЕГО: {len(store)}")
    print("- "*46)
    print(f"ВЫБОРКА: список оборудования отдела {Const.LOCATION_DEPARTMENT_SALE}:")
    store(location=Const.LOCATION_DEPARTMENT_SALE)

    print("- "*46)
    print(f"Получение списка как итератора (без выборки)")
    for i, item in enumerate(store, start=1):
        print(f"{i:03d}--{item}")


# Поехали
if __name__ == "__main__":
    main()
    print("End")
