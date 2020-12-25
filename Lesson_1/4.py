# Task 4 - я его так и не догадался как делать.

n = int(input('Введите целое положительное число - '))
max = n % 10

if n > 0:
    while n > 0:
        num = n % 10
        if num > max:
            max = num
        n = n // 10
        print(n)
    print(f'Самая большая цифра {max}')
else: print('Нужно было целое положительное число')

