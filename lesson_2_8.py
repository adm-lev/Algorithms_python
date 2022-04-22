"""
https://drive.google.com/file/d/1lbDmorKEVNW1aGfTm4FM3Sv3kPy9e2-2/view?usp=sharing
Посчитать, сколько раз встречается определенная цифра в
введенной последовательности чисел. Количество вводимых чисел и
цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

"""


def count(numb, k):
    if numb < 10:
        if numb == k:
            return 1
        else:
            return 0
    elif numb % 10 == k:
        return 1 + count(numb // 10, k)
    else:
        return count(numb // 10, k)


digit = int(input('Введите, пожалуйста, искомую цифру, '
                  'а затем несколько чисел и число ноль '
                  'для завершения ввода.\nЦифра: '))
temp = 0
while True:
    num = int(input('Число: '))
    if num:
        temp += count(num, digit)
    else:
        break
print(f'Указанная цифра встречается {temp} раз')






