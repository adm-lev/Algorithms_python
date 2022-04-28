"""

Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать
 ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.

"""


def show_matrix(matrix):
    tab = 9
    print(f' ' * (len(matrix[0]) * tab) + 'Сумма')
    for line in matrix:
        for item in line:
            print(f'{item:>{tab}}', end=' ')
        print('\n')


def calc_sum(matrix):
    for line in matrix:
        temp = 0
        for n, cell in enumerate(line):
            temp += line[n - 1]
        line.append(temp)


#  Заполнение матрицы
my_matrix = []
i = 0
print('Заполните, пожалуйста, матрицу 5 строк, 3 колонки значениями, '
      'разделяя числа пробелами, а строки клавишей "Enter"')
#  введенная строка разделяется по пробелам, элементы преобразуются
#  к типу int, список добавляется к матрице
while i < 5:

    my_matrix.append([int(item) for item in (input(f'ряд:{i+1}  ')).split()])
    i += 1


calc_sum(my_matrix)
show_matrix(my_matrix)




