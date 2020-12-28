# Task 4
n = input('Введите слова через пробел - ')
n = n.split()
for i, el in enumerate(n, 1):
    el = el[0:10]
    print(i, el)
