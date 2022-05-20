"""

Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартал (т.е. 4 числа) для каждого предприятия. Программа должна определить
среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования
предприятий, чья прибыль выше среднего и ниже среднего.

"""

from collections import namedtuple

Company = namedtuple('Company', 'name quart1 quart2 quart3 quart4 yearly')

number = int(input('Здравствуйте! Введите, пожалуйста, общее число представленных компаний: '))
all_companies = []
income = 0
avg_income = 0
profitable = []
unprofitable = []


def print_res(org_list):
    for _ in org_list:
        print(_, end='; ')


for i in range(number):                                      #  На основе пользовательских данных
    name = input(f'Введите имя {i + 1} компании: ')          #  создается объект типа Company
    quart1 = int(input(f'Введите прибыль за 1 квартал: '))
    quart2 = int(input(f'Введите прибыль за 2 квартал: '))
    quart3 = int(input(f'Введите прибыль за 3 квартал: '))
    quart4 = int(input(f'Введите прибыль за 4 квартал: '))

    all_companies.append(Company(name, quart1, quart2, quart3, quart4,
                                 quart1 + quart2 + quart3 + quart4))
    income += all_companies[i].yearly

avg_income = income / number

for i in all_companies:                                       #  Участники делятся на уловно прибыльных и убыточных
    if i.yearly >= avg_income:
        profitable.append(i.name)
    else:
        unprofitable.append(i.name)

print(f'Средняя прибыль равна: {avg_income}\nПрибыльные организации: ')
print_res(profitable)
print('\nУбыточные организации: ')
print_res(unprofitable)








