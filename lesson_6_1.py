"""

Среди натуральных чисел, которые были введены,
найти наибольшее по сумме цифр. Вывести на экран это
число и сумму его цифр.

"""
from memory_profiler import profile
from sys import getsizeof
import decimal
import tracemalloc
from guppy import hpy


def size_record(data):
    global overall
    overall += getsizeof(data)
    if hasattr(data, '__iter__'):
        if hasattr(data, 'items'):
            for key, value in data.items():
                size_record(key)
                size_record(value)
        elif not isinstance(data, str):
            for item in data:
                size_record(item)


# @profile
def int_way():
    def iter_count(numb):
        spam = 0
        while numb:
            spam += numb % 10
            numb //= 10
        return spam
    my_sum = record = res = 0
    print('Введите ряд чисел и число ноль для завершения')
    while True:
        num = int(input('Число: '))
        if num:
            res = iter_count(num)
        else:
            break
        if res > my_sum:
            my_sum = res
            record = num
    size_record(num)
    size_record(record)
    size_record(my_sum)
    size_record(res)
    print(f'Число с наибольшей суммой ({my_sum}): - {record}')


# @profile
def float_way():
    def iter_count(numb):
        spam = 0
        while numb:
            spam += numb % 10
            numb //= 10
        return spam
    my_sum = record = res = 0.0
    print('Введите ряд чисел и число ноль для завершения')
    while True:
        num = float(input('Число: '))
        if num:
            res = iter_count(num)
        else:
            break
        if res > my_sum:
            my_sum = res
            record = num
    size_record(num)
    size_record(record)
    size_record(my_sum)
    size_record(res)
    print(f'Число с наибольшей суммой ({my_sum}): - {record}')


def dec_way():
    def iter_count(numb):
        spam = 0
        while numb:
            spam += numb % 10
            numb //= 10
        return spam
    my_sum = record = res = decimal.Decimal(0)
    print('Введите ряд чисел и число ноль для завершения')
    while True:
        num = decimal.Decimal((input('Число: ')))

        if num:
            res = iter_count(num)
        else:
            break
        if res > my_sum:
            my_sum = res
            record = num
    size_record(num)
    size_record(record)
    size_record(my_sum)
    size_record(res)

    print(f'Число с наибольшей суммой ({my_sum}): - {record}')


if __name__ == "__main__":




    tracemalloc.start()

    overall = 0

    # int_way()            #  Числа: 1234, 2345, 3456. Банк памяти: 108 байт
    # float_way()          #  Числа: 1234, 2345, 3456. Банк памяти: 96 байт
    # dec_way()              #  Числа: 1234, 2345, 3456. Банк памяти: 416 байт

    print(overall)

h = hpy()

print(h.heap())





"""

Представлено три простых варианта решения задачи, использующих разные типы данных.
Оценка затрат памяти - многостороннее понятие, т.к. в разные моменты работы программы в 
пямяти может находиться различное количество значений. Например, в начале объявлены 3 переменые с литералом "0",
Это одна ячейка памяти. К концу работы функции на "0" указывает только record, но и он 
быстро перезаписывается, освобождая ячейку. Переменная numb также является временной, живя в теле функции iter_count.
На сколько я понимаю, до конца работы программы доживают лишь две из четырех переменных.

Но переменная overall хранит сумму всех неповторяющихся затрат памяти, как требовалось в условии. 
  
И, вполне ожидаемо, при использовании типа Decimal мы видим существенное увеличение использованной памяти, а при 
float - экономию. Его можно использовать, если не требуется деление с высокой точностью, как в этой программе 

"""


