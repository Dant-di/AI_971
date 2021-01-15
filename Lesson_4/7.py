# Task 7
def fact(n):
    factorial = 1
    if n == 0:
        yield 1
    for el in range(1, n+1):
        factorial = factorial * el
        yield factorial


for elem in fact(5):
    print(elem)
