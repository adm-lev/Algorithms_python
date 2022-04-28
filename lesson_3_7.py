"""

В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так
и различаться.

"""

from condition import array


def two_values(arr):
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


print(f'Дан массив: {array}')
result = two_values(array)
print(f'Два минимальных элемента: {result[0]} и {result[1]}')



















