"""

2). Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

"""
from random import randint, randrange


arr = [randrange(0, 50) for _ in range(10)]


def merge_sort(data):
    if len(data) <= 1:
        return data
    middle = len(data) // 2
    left_part = merge_sort(data[:middle])[::-1]
    right_part = merge_sort(data[middle:])[::-1]
    result = []
    while left_part and right_part:
        result.append(left_part.pop() if left_part[-1] < right_part[-1] else right_part.pop())
    if not left_part:
        if right_part:
            result.extend(right_part[::-1])
    elif not right_part:
        if left_part:
            result.extend(left_part[::-1])
    return result


print(arr)
print(merge_sort(arr))

