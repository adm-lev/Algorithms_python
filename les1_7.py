"""
начало

вывод: укажите длины трех отрезков
записать значение отрезка A
записать значение отрезка B
записать значение отрезка C
если A >= B
    если A >= C
        если B >= C
            max = A
            mid = B
            min = C
        иначе
            max = A
            mid = C
            min = B
    иначе
        max = C
        mid = A
        min = B
иначе если B >=C
    если A >=C
        max = В
        mid = А
        min = C
    иначе
        max = B
        mid = C
        min = A
иначе
    max = C
    mid = B
    min = A

если min == mid == max
    вывод: треугольник равтосторонний
иначе если max >= mid + min
    вывод: треугольник построить невозможно
иначе если mid == min
    вывод: треугольник равнобедренный
иначе
    вывод: треугольник разносторонний

    конец
"""

print('Укажите длину каждого из отрезков: ')
side_a = int(input('Длина А: '))
side_b = int(input('Длина B: '))
side_c = int(input('Длина C: '))
if side_a >= side_b:
    if side_a >= side_c:
        if side_b >= side_c:
            max_side = side_a
            mid_side = side_b
            min_side = side_c
        else:
            max_side = side_a
            mid_side = side_c
            min_side = side_b
    else:
        max_side = side_c
        mid_side = side_a
        min_side = side_b
elif side_b >= side_c:
    if side_a >= side_c:
        max_side = side_b
        mid_side = side_a
        min_side = side_c
    else:
        max_side = side_b
        mid_side = side_c
        min_side = side_a
else:
    max_side = side_c
    mid_side = side_b
    min_side = side_a

print(f'max {max_side}')
print(f'mid {mid_side}')
print(f'min {min_side}')

if max_side == mid_side == min_side:
    print('Треугольник равносторонний')
elif max_side >= (min_side + mid_side):
    print('Треугольник построить невозможно')
elif min_side == mid_side:
    print('Треугольник равнобедренный')
else:
    print('Треугольник разносторонний')










