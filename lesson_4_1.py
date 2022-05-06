"""

В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так
и различаться.

"""

from random import randint
import timeit
import sys
import matplotlib.pyplot as plt



sys.setrecursionlimit(2000)
AMOUNT = 1000
MIN = 0
MAX = 10000

#  Блок объявления функций, находящих минимальные числа:


def two_values(arr):   #  Первый вариант функции, взятый из решения к 3-му уроку. Использована рекурсия.
    if len(arr) == 2:
        if arr[0] > arr[1]:
            return [arr[1], arr[0]]
        return [arr[0], arr[1]]
    temp = two_values(arr[1:])
    if arr[0] <= temp[0]:
        temp[0], temp[1] = arr[0], temp[0]
    elif temp[0] < arr[0] < temp[1]:
        temp[1] = arr[0]
    return temp


def two_values_improved(arr):  #  Второй вариант функции, выполненный через цикл for. По скорости опережает другие
    temp = [arr[0]] * 2
    for i in arr:
        if i < temp[0]:
            temp[0], temp[1] = i, temp[0]
        elif temp[0] < i < temp[1]:
            temp[1] = i
    return temp


def two_values_retarded(arr):   #  В этой версии выполняется пузырьковая сортировка массива,
                                # а затем возвращаются два первых элемента. Он очень медленный
    messed = True
    while messed:
        messed = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                messed = True
    temp = arr[:2]
    return temp


#  Блок тестовых функций, с предачей различных значений длины массива


def get_time(func, n):      #  Создается массив необходимого размера, с которым работает timeit
    array = [randint(MIN, MAX) for _ in range(int(n))]
    return timeit.timeit(f'{func}({array})', number=AMOUNT, globals=globals())


def calc_dependencies(x, y, function):     #  Здесь результаты timeit помещаются в массивы
    var = 10                               #  для удобного графического отображения.
    while var < 1900:                      #  Стоит подробнее остановиться на выбранных мною цифрах.
        y.append(get_time(function, var))  #  К сожалению, максимальная длина упирается в переполнение стека,
        x.append(var)                      #  который немного увеличил, чтобы дать хоть какое-то пространство
        var *= 10                          #  для наглядности результата(не хотелось исключать из сравнения
        print(var)                         #  вариант с рекурсией). Остальные числа подобраны для
                                           #  достаточного количества точек на графике функции.

# print(f'Дан массив: {array}')
# result = two_values_improved(array)
# print(f'Два минимальных элемента: {result[0]} и {result[1]}')

#  Блок сравнения результатов. По парным массивам данных строятся разноцветные графики


y1 = list()
x1 = list()
x2 = list()
y2 = list()
x3 = list()
y3 = list()

calc_dependencies(x1, y1, 'two_values')
calc_dependencies(x2, y2, 'two_values_improved')
calc_dependencies(x3, y3, 'two_values_retarded')
print(f'x1 {x1}')
print(f'y1 {y1}')
print(f'x2 {x2}')
print(f'y2 {y2}')
print(f'x3 {x3}')
print(f'y3 {y3}')

plt.figure(figsize=(12, 12))
plt.plot(x1, y1, 'o-g', alpha=0.7, label="first recursive function", lw=5, mec='b', mew=1, ms=5)
plt.plot(x2, y2, 'o-r', alpha=0.7, label="second version with cycle", lw=2, mec='b', mew=2, ms=5)
plt.plot(x3, y3, 'o-c', alpha=0.7, label="third one, with a bubble sort", lw=2, mec='b', mew=2, ms=5)
plt.legend()
plt.grid(True)
plt.show()

"""

Исследование показало, что простой перебор значений через цикл справляется с задачей быстрее,
чем рекурсивный способ. 

"""







