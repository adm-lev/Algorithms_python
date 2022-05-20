"""

Написать программу сложения и умножения двух положительных целых
шестнадцатеричных чисел. При этом каждое число представляется как коллекция,
элементы которой — цифры числа. Например, пользователь ввёл A2 и C4F.
Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

"""

from collections import deque


num_a = deque('F1E4D')
num_b = deque('1221D478E')
num_c = deque('123')
num_d = deque('123')


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


def get_raw(c, d):
    # print(f'c and d: {c}  {d}')
    memory = 0
    # oper = int(d.pop())
    res = deque()

    while c:
        calc = int(c.pop()) * int(d) + memory
        res.appendleft(calc % 10)
        memory = calc // 10
    if not c:
        res.appendleft(memory)
    # print(f'currentrow  {res}')
    return res


def dec_product(a, b):
    memory = 0
    place = 0
    rows = []

    while b:
        f = b.pop()

        print(f'a and b: {a}   {f}')
        temp_row = get_raw(a, f)
        # print(f'temprow: {temp_row}')
        for i in range(place):
            temp_row.append(0)
        rows.append(temp_row)
        # print(rows)
        place += 1
    res = rows[0]

    for i in range(1, len(rows)):
        res = dec_sum(res, rows[i])
    return res






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

"""

код с ошибкой. При вычислении произведения, выдает неверный результат. Почему?

"""



# print(dec_sum(num_c, num_d))
# print(hex_sum(num_a, num_b))
print(dec_product(num_c, num_d))




