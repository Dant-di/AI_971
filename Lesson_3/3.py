# Task 3
def func(a, b, c):

    if a == min(a, b, c):
        return b + c
    elif b == min(a, b, c):
        return a + c
    elif c == min(a, b, c):
        return a + b
    else:
        return a + b


x = int(input('Введите превое число - '))
y = int(input('Введите второе число - '))
z = int(input('Введите третье число - '))


print(f'Сумма двух наибольших чисел равна - {func(x, y, z)}')
