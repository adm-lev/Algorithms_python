"""

 Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
 Количество элементов (n) вводится с клавиатуры

"""


def sum_row(numb):

    if numb == 1:
        return numb
    else:
        oper = numb
        term = 1
        while oper > 1:
            term /= -2
            oper -= 1
        sum = sum_row(numb - 1)

        return sum + term


num = int(input('введите положительное число: '))

print(sum_row(num))


