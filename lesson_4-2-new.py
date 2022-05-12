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


AMOUNT = 1000                                   #  одинокая переменная


def get_simple_ver3(num):

    i = 2  # счетчик найденных простых чисел
    cur_simple = 5  # текущее простое число
    cur_checked = 3  # проверяемое число
    if num == 1 or num == 2:
        return num + 1
    memo = [3]
    while i < num:
        cur_checked += 2  # шаг в 2 числа избавляет от проверки четных чисел
        compos_detect = False
        divisor = int(cur_checked ** 0.5)  # наименьший делитель не больше квадратного корня из проверяемого числа
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
    return cur_simple


def get_simple_sieve(num):
    stop = 100                                    #  Переменная размера первого массива
    start = 2                                     #  Точка старта первого массива
    arr = list()
    steps_memo = {2: 0, 3: 1, 5: 3, 7: 5, 11: 9}  #  Словарь чисел и стартовых позиций для вычеркивания

    while True:                                   #  Этот цикл будет повторяться если размера массива не хватит
        new_arr = [i for i in range(start, stop)] #  Первый массив, а также все добавленные
        arr += new_arr
        size = len(arr)                           #  Часто встречающееся значение
        stop = size * 2
        start = arr[-1] + 1

        for key, value in steps_memo.items():
            for i in range(value + key, size, key):  #  Вычеркивание значений и обновление позиций в словаре
                arr[i] = 0
                steps_memo[key] = i

        for i in range(size):                        #  Проверка и добавленние новых значений в словарь
            if arr[i] and arr[i] not in steps_memo and arr[i] < size:
                steps_memo[arr[i]] = i

        simple_arr = [i for i in arr if i]           #  Высыпание и пересчет просеянных значений
        if len(simple_arr) > num:
            break

    return simple_arr[num - 1]


def calc_dependencies(x, y, function):               #  Этот блок тестирует функцию в диапазоне значений и
    var = 10                                         #  сохраняет результаты для удобного вывода на графике
    while var <= 2000:                               #  Подставные значения выбраны для баланса между красивым графиком
        y.append(timeit.timeit(f'{function}({var})', number=AMOUNT, globals=globals()))
        x.append(var)                                #  и не слишком долгим ожиданием
        var += 50


"""  ==========================Часть проверки функций========================  """

print(get_simple_ver3(5000))
print(get_simple_sieve(5000))

"""  ========================Тестовая графическая часть============================="""

x3 = list()
y3 = list()
x4 = list()
y4 = list()

calc_dependencies(x3, y3, 'get_simple_ver3')
calc_dependencies(x4, y4, 'get_simple_sieve')
plt.figure(figsize=(10, 10))

plt.plot(x3, y3, 'o-c', alpha=0.7, label="with memoisation", lw=2, mec='b', mew=2, ms=5)
plt.plot(x4, y4, 'o-y', alpha=0.7, label="with sieve", lw=2, mec='b', mew=2, ms=5)
plt.legend()
plt.grid(True)
plt.show()

"""   =========================разбор работы функции в cProfile==========================   """

cProfile.run('get_simple_ver3(5000)')
cProfile.run('get_simple_sieve(5000)')


"""

Было реализовано множество функций, основанных на простой проверке делимости чисел. 
В коде представлена самая быстрая версия из тех, что без принципа Решета Эратосфена.

Реализация функции с "Решетом" далась мне тяжелее первой, но ожидания не вполне оправдала.
Ее полезность критически зависит от избыточности размера взятого массива

"""
