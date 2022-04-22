"""
https://drive.google.com/file/d/1lbDmorKEVNW1aGfTm4FM3Sv3kPy9e2-2/view?usp=sharing
Напишите программу, доказывающую или проверяющую,
что для множества натуральных чисел выполняется равенство:
1+2+...+n = n(n+1)/2, где n — любое натуральное число.

"""


def get_sum(num):
    if num == 1:
        return num
    else:
        res = num + get_sum(num - 1)
        return res


n = int(input('Введите длину множества: '))
sum = get_sum(n)
formula = int(n * (n + 1) / 2)

print(f'По формуле:{formula} \nВручную:  {sum}')
if sum == formula:
    print('Теорема проверена!')
else:
    print('Математики всё врут!')