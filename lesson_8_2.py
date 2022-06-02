"""

2) Закодируйте любую строку по алгоритму Хаффмана.
Превратитет строку текста в строку из нулей и единиц - визуальное текстовое представление сжатие данных.

"""

import collections

sample = 'beep boop beer!'
c = collections.Counter(sample)

print(c)


class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.value}\n{self.left} - {self.right}'

my_tree = {}

while True:
    
