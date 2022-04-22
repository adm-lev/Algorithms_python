"""
https://drive.google.com/file/d/1lbDmorKEVNW1aGfTm4FM3Sv3kPy9e2-2/view?usp=sharing
Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5)

"""


def evenodd(nums, even=True):

    if even:
        #  Базовый случай, если осталось одно число и оно четное
        if nums // 10 == 0:
            if nums % 2 == 0:
                return 1
            else:
                return 0
        else:
            #  стандартный случай, определяем четность крайнего числа,
            #  остальную чать снова передаем функции
            if (nums % 10) % 2 == 0:
                return 1 + evenodd(nums // 10)
            else:
                return evenodd(nums // 10)
    else:
        #  Базовый случай, если осталось одно число и оно нечетное
        if nums // 10 == 0:
            if nums % 2 != 0:
                return 1
            else:
                return 0
        else:
            #  стандартный случай, определяем четность крайнего числа,
            #  остальную чать снова передаем функции
            if (nums % 10) % 2 != 0:
                return 1 + evenodd(nums // 10, False)
            else:
                return evenodd(nums // 10, False)


num = int(input('Введите натуральное число: '))
eve = evenodd(num)
odd = evenodd(num, False)
print(f'число содержит {eve} четных и {odd} нечетных цифр')
