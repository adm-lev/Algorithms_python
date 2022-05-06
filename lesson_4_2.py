"""

 Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого
 числа должна принимать на вход натуральное и возвращать соответствующее простое число.
 Проанализировать скорость и сложность алгоритмов.

- Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте
этот код и попробуйте его улучшить/оптимизировать под задачу.

- Второй — без использования «Решета Эратосфена».
Примечание. Вспомните классический способ проверки числа на простоту.

"""
import timeit
import matplotlib.pyplot as plt
import cProfile

#  Простые числе после 2 - только нечетные
#  Наименьший делитель не превосходит квадратный корень из числа


# limit = int(input('Введите номер искомого простого числа: '))
AMOUNT = 100
counter = 0


def get_simple(num):
    global counter
    i = 2                                    #  счетчик найденных простых чисел
    cur_simple = 5                           #  текущее простое число
    cur_checked = 3                          #  проверяемое число
    if num == 1 or num == 2:
        return num + 1

    while i < num:
        cur_checked += 2
        compos_detect = False
        for j in range(2, cur_checked):
            if cur_checked % j == 0:
                compos_detect = True
                break
        if compos_detect:
            continue
        cur_simple = cur_checked
        i += 1
    return cur_simple


def get_simple_ver2(num):
    global counter
    i = 2                                    #  счетчик найденных простых чисел
    cur_simple = 5                           #  текущее простое число
    cur_checked = 3                          #  проверяемое число
    if num == 1 or num == 2:
        return num + 1

    while i < num:
        cur_checked += 2
        compos_detect = False
        divisor = int(cur_checked ** 0.5) + 1
        for j in range(2, divisor):
            if cur_checked % j == 0:
                compos_detect = True
                break
        if compos_detect:
            continue
        cur_simple = cur_checked
        i += 1
    return cur_simple


def get_simple_ver3(num):
    global counter
    i = 2                                    #  счетчик найденных простых чисел
    cur_simple = 5                           #  текущее простое число
    cur_checked = 3                          #  проверяемое число
    if num == 1 or num == 2:
        return num + 1
    memo = [3]
    while i < num:
        cur_checked += 2                      #  шаг в 2 числа избавляет от проверки четных чисел
        compos_detect = False
        divisor = int(cur_checked ** 0.5)  #  наименьший делитель не больше квадратного корня из проверяемого числа
        for j in memo:
            if j > divisor:
                break
            if cur_checked % j == 0:
                compos_detect = True
                break
        if compos_detect:
            continue
        cur_simple = cur_checked
        memo.append(cur_checked)
        i += 1
    # print(memo)
    return cur_simple


def calc_dependencies(x, y, function):
    var = 10
    while var <= 10000:
        y.append(timeit.timeit(f'{function}({var})', number=AMOUNT, globals=globals()))
        x.append(var)
        var += 50
        print(var)


"""  ==========================Часть отладки функций========================  """

# print(get_simple_ver3(500))






"""  ================Тестовая графическая часть============================="""
x1 = list()
y1 = list()
x2 = list()
y2 = list()
x3 = list()
y3 = list()

# calc_dependencies(x1, y1, 'get_simple')
# calc_dependencies(x2, y2, 'get_simple_ver2')
calc_dependencies(x3, y3, 'get_simple_ver3')

print(f'x1 - {x1}')
print(f'y1 - {y1}')
print(f'x2 - {x2}')
print(f'y2 - {y2}')
print(f'x3 - {x3}')
print(f'y3 - {y3}')


plt.figure(figsize=(10, 10))
# plt.plot(x1, y1, 'o-g', alpha=0.7, label="1) with simple enumeration", lw=5, mec='b', mew=1, ms=5)
# plt.plot(x2, y2, 'o-r', alpha=0.7, label="second version with cycle", lw=2, mec='b', mew=2, ms=5)
plt.plot(x3, y3, 'o-c', alpha=0.7, label="third one, with a bubble sort", lw=2, mec='b', mew=2, ms=5)
plt.legend()
plt.grid(True)
plt.show()

"""   ===========================разбор работы функции в cProfile==========================   """
# cProfile.run('get_simple(5000)')
# cProfile.run('get_simple_ver2(5000)')
# cProfile.run('get_simple_ver3(5000)')








