"""

Программа суммирует или умножает десятичные числа в столбик

"""

from collections import deque
import copy


num_c = deque('99490')
num_d = deque('11999')


def dec_sum(a, b):
    memory = 0
    res = deque()
    while True:
        if not a and b:
            calc = int(b.pop()) + memory
        elif not b and a:
            calc = int(a.pop()) + memory
        else:
            calc = int(a.pop()) + int(b.pop()) + memory

        if calc >= 10:
            res.appendleft(calc % 10)
            memory = calc // 10
        else:
            res.appendleft(calc)
            memory = 0
        if not a and not b:
            res.appendleft(memory)
            break

    return res


def get_raw_dec(c, d):
    memory = 0
    res = deque()

    while c:
        calc = int(c.pop()) * int(d) + memory
        res.appendleft(calc % 10)
        memory = calc // 10
    if not c:
        res.appendleft(memory)
    return res


def dec_product(a, b):

    place = 0
    rows = []

    while b:

        temp_a = copy.copy(a)
        temp_row = get_raw_dec(temp_a, b.pop())

        for i in range(place):
            temp_row.append(0)
        rows.append(temp_row)

        place += 1
    res = rows[0]

    for i in range(1, len(rows)):
        res = dec_sum(res, rows[i])

    # while True:
    #     if res[0] == '0':
    #         res.popleft()
    #     else:
    #         break

    return res


def print_deque(my_deque):

    while my_deque:
        print(my_deque.popleft(), end='')


# print(dec_sum(num_c, num_d))
print(dec_product(num_c, num_d))
