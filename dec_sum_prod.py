"""

Написать программу сложения и умножения двух положительных целых
шестнадцатеричных чисел. При этом каждое число представляется как коллекция,
элементы которой — цифры числа. Например, пользователь ввёл A2 и C4F.
Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

"""

from collections import deque
import copy


# num_a = deque('ABCD')
# num_b = deque('DCBA')
# num_c = deque('9990')
# num_d = deque('11999')


# def dec_sum(a, b):
#     memory = 0
#     res = deque()
#     while True:
#         if not a and b:
#             calc = int(b.pop()) + memory
#         elif not b and a:
#             calc = int(a.pop()) + memory
#         else:
#             calc = int(a.pop()) + int(b.pop()) + memory
#
#         if calc >= 10:
#             res.appendleft(calc % 10)
#             memory = calc // 10
#         else:
#             res.appendleft(calc)
#             memory = 0
#         if not a and not b:
#             res.appendleft(memory)
#             break
#
#     return res


def hex_sum(a, b):
    memory = 0
    res = deque()
    while True:
        if not a and b:
            calc = translate_to_dec[b.pop()] + memory
        elif not b and a:
            calc = translate_to_dec[a.pop()] + memory
        else:
            calc = translate_to_dec[a.pop()] + translate_to_dec[b.pop()] + memory

        if calc >= 16:
            res.appendleft(translate_to_hex[calc % 16])
            memory = calc // 16
        else:
            res.appendleft(translate_to_hex[calc])
            memory = 0

        if not a and not b:
            res.appendleft(translate_to_hex[memory])
            break

    return res


# def get_raw_dec(c, d):
#     memory = 0
#     res = deque()
#
#     while c:
#         calc = int(c.pop()) * int(d) + memory
#         res.appendleft(calc % 10)
#         memory = calc // 10
#     if not c:
#         res.appendleft(memory)
#     return res


def get_raw_hex(c, d):
    memory = 0
    res = deque()

    while c:
        calc = translate_to_dec[c.pop()] * translate_to_dec[d] + memory
        res.appendleft(translate_to_hex[calc % 16])
        memory = calc // 16
    if not c:
        res.appendleft(translate_to_hex[memory])
    return res


# def dec_product(a, b):
#
#     place = 0
#     rows = []
#
#     while b:
#
#         temp_a = copy.copy(a)
#         temp_row = get_raw_dec(temp_a, b.pop())
#
#         for i in range(place):
#             temp_row.append(0)
#         rows.append(temp_row)
#
#         place += 1
#     res = rows[0]
#
#     for i in range(1, len(rows)):
#         res = dec_sum(res, rows[i])
#     return res


def hex_product(a, b):
    place = 0
    rows = []

    while b:
        temp_a = copy.copy(a)
        temp_row = get_raw_hex(temp_a, b.pop())

        for i in range(place):
            temp_row.append('0')
        rows.append(temp_row)

        place += 1
    res = rows[0]

    for i in range(1, len(rows)):
        res = hex_sum(res, rows[i])

    while True:
        if res[0] == '0':
            res.popleft()
        else:
            break

    return res


def print_deque(my_deque):

    while my_deque:
        print(my_deque.popleft(), end='')


translate_to_hex = {
    0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5',
    6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B',
    12: 'C', 13: 'D', 14: 'E', 15: 'F'
}
translate_to_dec = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
    '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
    'C': 12, 'D': 13, 'E': 14, 'F': 15
}


num_a = deque(input('Введите первое шестнадцатеричное число:').upper())
oper = input('Введите знак операции(* или +)')
num_b = deque(input('Введите второе шестнадцатеричное число:').upper())

if oper == '*':
    print_deque(hex_product(num_a, num_b))
else:
    print_deque(hex_sum(num_a, num_b))

# print(dec_sum(num_c, num_d))
# print(hex_sum(num_a, num_b))
# print(dec_product(num_c, num_d))
# print((hex_product(num_a, num_b)))