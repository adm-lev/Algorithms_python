"""

Найти максимальный элемент среди минимальных элементов столбцов матрицы.

"""

from condition import matrix


def show_matrix(mat):
    tab = 9
    for row in mat:
        for item in row:
            print(f'{item:>{tab}}', end=' ')
        print('\n')


show_matrix(matrix)
# print(*matrix, sep='\n')

results = matrix[0]
maximum = 0
#  Составить список из наименьших элементов столбцов
for line in matrix:
    for k, cell in enumerate(line):
        if cell < results[k]:
            results[k] = cell

#  выбрать победителя
for i in range(len(results)):
    if maximum < results[i]:
        maximum = results[i]


print(f'Наибольший из минимальных элементов столбцов: {maximum}')
