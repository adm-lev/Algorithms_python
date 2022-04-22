"""
https://drive.google.com/file/d/1lbDmorKEVNW1aGfTm4FM3Sv3kPy9e2-2/view?usp=sharing
Среди натуральных чисел, которые были введены,
найти наибольшее по сумме цифр. Вывести на экран это
число и сумму его цифр.

"""


def count(numb):
    if numb < 10:
        return numb
    else:
        return numb % 10 + count(numb // 10)


sum = res = rec = 0

print('Введите ряд чисел и число ноль для завершения')
while True:
    num = int(input('Число: '))
    if num:
        res = count(num)
    else:
        break
    if res > sum:
        sum = res
        rec = num

print(f'Число с наибольшей суммой({sum}) - {rec}')









