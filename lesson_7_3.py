"""

3). Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.

Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).

"""
from random import randrange
import collections
from lesson_7_1 import bubble_sort


length = int(input(f'Введите натуральное число: '))
arr = [randrange(-100, 100) for _ in range(2 * length + 1)]


def new_med(data):

    c = collections.Counter(data)            #  Создается счетчик элементов массива
    min_elem = data[0]
    min_times = 0
    sorted_index = 0

    while True:

        for i in c.keys():
            if i <= min_elem:                #  Случай когда нашли минимальный элемент
                min_elem = i                 #  Запоминаем этот элемент
                min_times = c[i]             #  а также число его повторений

        sorted_index += min_times            #  Прикидываем индекс элемента в гипотетически отсортированном массиве

        if sorted_index >= len(data) // 2 + 1:  #  Если индекс перевалили за середину - возвращаем элемент
            return min_elem

        del c[min_elem]                      #  Убираем элемент из счетчика для будущих итераций
        for k, v in c.items():               #  Быть может, не самый ловкий способ найти первый элемент словаря
            min_elem = k                     #  но рабочий
            break


def check(func_a, func_b, my_length):              #  Функция тестирования, подключая сортировку из первой задачи
                                                   #  и сравнивая средний элемент отсортированного списка с результатом
    for _ in range(100):
        my_arr = [randrange(-100, 100) for _ in range(2 * my_length + 1)]
        a = func_a(my_arr)
        b = func_b(my_arr)[len(my_arr) // 2]
        if a == b:
            # print(my_arr)
            print(f' ok {a} = {b}')
        else:
            # print(my_arr)
            print(f'not ok {a} != {b}')



# print(arr)
# print(new_med(arr))
bubble_sort(arr)
# print(f'bubble:  {arr}')


# check(new_med, bubble_sort, length)




