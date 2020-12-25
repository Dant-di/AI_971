# Task 5
revenue = int(input('Введите выручку фирмы - '))
cost = int(input('Введите затраты фирмы - '))

if revenue > cost:
    print('Ура! С прибылью!')
    profit = (revenue - cost) / cost
    print('Ваша рентабельность:' + str(profit))

    pers = int(input('Введите количество сотрудников - '))
    print('Прибыль фирмы на одного сотрудника - ' + str(profit/pers))
elif revenue < cost:
    print('Увы, убытки. Оптимизируйте затраты')
else:
    print('Вышли в ноль')
