# Task 7

class Cmplx:

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        sum_real = self.real + other.real
        sum_imag = self.imag + other.imag
        sign = ''
        sign = '+' if sum_imag >= 0 else sign
        return f'({sum_real}{sign}{sum_imag}i)'

    def __mul__(self, other):
        if self.real == 0 and self.imag == 0:
            return f'-0i'
        elif other.real == 0 and other.imag == 0:
            return f'-0i'
        else:
            mul_real = (self.real*other.real - self.imag*other.imag)
            mul_imag =  (self.real * other.imag + self.imag * other.real)
            sign = ''
            sign = '+' if mul_imag >= 0 else sign
            return f'({mul_real}{sign}{mul_imag}i)'

    def __str__(self):
        sign = ''
        sign = '+' if self.imag >= 0 else sign
        if self.real == 0:
            return f'({self.imag}i)'
        else:
            self.out = f'({self.real}{sign}{self.imag}i)'
            return self.out


a = Cmplx(5, -6)
b = Cmplx(2, 7)

print('Class values')
print(f'Complex numbers: {a}, {b}')
print(f'Sum of complex numbers: {a + b}')
print(f'Multiplication of complex numbers: {a * b}\n')

x = complex(5, -6)
y = complex(2, 7)

print('Control values:')
print(f'Complex numbers: {x, y}')
print(f'Sum of complex numbers: {x + y}')
print(f'Multiplication of complex numbers: {x * y}\n')
