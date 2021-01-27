# Task 1

class Matrix:

    def __init__(self, matr):
        self.matr = matr

    def __str__(self):
        self.line = ''
        for el in self.matr:
            self.line += ' '.join(map(str, el)) + '\n'
        return self.line

    def __add__(self, other):
        self.res_matr = []
        for x in zip(self.matr, other.matr):
            self.tmp = []
            for y in zip(x[0], x[1]):
                self.tmp.append(sum(y))
            self.res_matr.append(self.tmp)
        return Matrix(self.res_matr)


a = Matrix([[41, 2, 8, 4], [17, 1, 0, -1],[62, 3, 7, 0]])
b = Matrix([[36, 5, -1, 3], [71, 7, 8, 9],[37, 6, 2, 9]])


print(f'Matrix #1:\n{a}')
print(f'Matrix #2: \n{b}')
print(f'Sum of matrices 1 and 2:\n{a + b}')
