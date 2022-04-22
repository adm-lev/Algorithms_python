"""
Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения вычисления
программа не завершается, а запрашивает новые данные для вычислений. Завершение
программы должно выполняться при вводе символа '0' в качестве знака операции. Если
пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), программа должна сообщать
об ошибке и снова запрашивать знак операции. Также она должна сообщать пользователю
о невозможности деления на ноль, если он ввел его в качестве делителя.

"""


def calc(f, s, o):

    if o == '+':
        return f + s
    if o == '/':
        if s == 0:
            return 'на ноль делить нельзя'
        else:
            return f / s
    if o == '*':
        return f * s
    if o == '-':
        return f - s
    else:
        return 'не знаем такого знака :-('


print('Вас приветствует программа-калькулятор')
while True:
    first = int(input('Введите целое положительное число: '))
    operator = input('Введите знак операции: ')
    if operator == '0':
        print('До свидания!')
        break
    second = int(input('Введите следующее целое положительное число'))

    res = calc(first, second, operator)
    print(res)














