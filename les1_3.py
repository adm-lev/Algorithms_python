"""
https://drive.google.com/file/d/1Zznq5iNIr304lXOhn2moZP3GF4zF5Rgi/view?usp=sharing
начало
вывод сообщения: введите по почереди координаты двух точек
записать значение х1
записать значение у1
записать значение х2
записать значение у2
проверка, не являются ли значения по x или y одинаковыми для обоих точек
если да, то вывод 1 соответствующей формулы и конец программы
вывод: получена следующая система уравнений
нахождение значения k = (-y2 + y1)/(x1 - x2)
нахождение значения b = -k * x1 + y1
емли b отрицательное - вывод 2
иначе - вывод 3

конец


"""

print('Здравствуйте! Укажите  поочередно координаты двух разных точек')
x_1 = float(input('введите x1  '))
y_1 = float(input('введите y1  '))
x_2 = float(input('введите x2  '))
y_2 = float(input('введите y2  '))

if x_1 == x_2:
    print(f'уравнение прямой:')
    print(f'  x = {x_1}')
elif y_1 == y_2:
    print(f'уравнение прямой:')
    print(f'  y = {y_1}')
else:
    print(f'Получена следующая система уравнений: '
          f'\n{y_1} = {x_1}k + b\n{y_2} = {x_2}k + b')
    k = (-1 * y_2 + y_1) / (x_1 - x_2)
    b = -1 * k * x_1 + y_1
    print(f'уравнение прямой:')
    print(f'  y = {k}x+{b}' if b >= 0 else f'y = {k}x{b}')
