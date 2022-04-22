"""
https://drive.google.com/file/d/1lbDmorKEVNW1aGfTm4FM3Sv3kPy9e2-2/view?usp=sharing
Сформировать из введенного числа обратное по
порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843

"""


def expandir(nums):
    if nums // 10 == 0:
        return nums
    else:
        return str(nums % 10) + str(expandir(nums // 10))


num = int(input('Введите натуральное число: '))

res = int(expandir(num))

print(f'перевернутое число: {res}')

