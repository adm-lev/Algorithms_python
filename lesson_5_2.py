"""

Написать программу сложения и умножения двух положительных целых
шестнадцатеричных чисел. При этом каждое число представляется как коллекция,
элементы которой — цифры числа. Например, пользователь ввёл A2 и C4F.
Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

"""

from collections import deque
import copy


def hex_sum(a, b):                                                                 #  Функция складывает числа в столбик
    memory = 0
    res = deque()
    while True:
        if not a and b:                                                            #  компенсация неравных длин чисел(1)
            calc = translate_to_dec[b.pop()] + memory
        elif not b and a:
            calc = translate_to_dec[a.pop()] + memory
        else:                                                                      #  перевести два крайних числа
            calc = translate_to_dec[a.pop()] + translate_to_dec[b.pop()] + memory  #  в десятичную и сложить,
                                                                                   #  добавив число из памяти.
        if calc >= 16:                                                             #  Записать единицы в резуультат,
            res.appendleft(translate_to_hex[calc % 16])                            #  а десятки в память
            memory = calc // 16
        else:
            res.appendleft(translate_to_hex[calc])
            memory = 0

        if not a and not b:                                                        #  компенсация неравных длин чисел(2)
            res.appendleft(translate_to_hex[memory])
            break

    return res


def get_raw_hex(c, d):                                                      #  Вспомогательная функция для умножения.
    memory = 0                                                              #  Умножает полное число на одну цифру.
    res = deque()

    while c:
        calc = translate_to_dec[c.pop()] * translate_to_dec[d] + memory
        res.appendleft(translate_to_hex[calc % 16])
        memory = calc // 16
    if not c:
        res.appendleft(translate_to_hex[memory])
    return res


def hex_product(a, b):
    place = 0
    rows = []

    while b:                                                                #  Получаем результаты произведения
        temp_a = copy.copy(a)                                               #  первого числа на каждый из
        temp_row = get_raw_hex(temp_a, b.pop())                             #  разрядов второго.

        for i in range(place):
            temp_row.append('0')
        rows.append(temp_row)

        place += 1
    res = rows[0]

    for i in range(1, len(rows)):                                            #  Суммируем значения известным способом
        res = hex_sum(res, rows[i])

    while True:                                                              #  Убираем появившиеся слева нули
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






