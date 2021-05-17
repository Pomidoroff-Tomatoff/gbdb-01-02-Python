# GeekBrains > Python basics: Oleg Gladkiy (https://geekbrains.ru/users/3837199)
# Lesson-1. 1-Variables
# 1. Поработайте с переменными, создайте несколько, выведите на экран,
#    запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

homework_type = "Lesson-1. 1-Variables"
print(homework_type)

i_int = int(
    input("--enter an integer number: "))
i_flt = float(
    input("--enter an real number: "))
i_str = (
    input("--enter a text line: "))
print("")

print("Вывод с ручным форматированием")
print("Integer value:",  str(i_int) + "\nText value:   \'" + i_str + "\'")
print("")

print("Вывод с форматированием при помощи оператора 'процент' (%)")
print("%16s %d" % ('Integer VALUE:', i_int))
print("%16s %.10f" % ('Float VALUE:', i_flt))
print("%16s %s" % ('String VALUE:', i_str))
print("")

print("Вывод при помощи метода .format()")
print("{0:>16} {1:>05d}".format("integer value:", i_int))
print("{0:>16} {1:<05d} {2}".format("integer value:", i_int, "(with error format output)"))
print("{0:>16} {1:< 021.10f}".format("float value:", i_flt))
print("{0:>16} {1:<20}".format("string value:", i_str))
print("")

# Вывод данных как f-строк
print("Вывод данных как f-строк")
print(f"integer value: {i_int}. Text string: «{i_str}»")
