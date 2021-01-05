# Task 1
def my_func(a, b):
    return float(a / b)


num1 = int(input('Введите делимое - '))
num2 = int(input('Введите делитель - '))
while num2 == 0:
    print('Делитель не может быть 0.')
    num2 = int(input('Введите делитель - '))

print(f'Ваше частное равно: {my_func(num1, num2).__round__(2)}')
