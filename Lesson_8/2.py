# Task 2

class ErrMac(Exception):

    def __init__(self, message):
        self.message = message


while True:
    a = int(input('Input first number - '))
    b = int(input('Input second number - '))
    try:
        if b == 0:
            raise ErrMac('What do we say to ZeroDivisionError? Not today! ')
    except ErrMac as error:
        print(error)
    else:
        print(f'Division result is {a / b}')
