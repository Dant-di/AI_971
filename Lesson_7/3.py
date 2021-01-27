# Task 3

class Cell:

    def __init__(self, cell_amount: int, cell_row: int):
        self.line = ''
        self.cell_amount = cell_amount
        self.cell_row = cell_row

    def __add__(self, other):
        return self.cell_amount + other.cell_amount

    def __sub__(self, other):
        if self.cell_amount < other.cell_amount:
            return 'Not possible to substract larger cell from smaller. Microbiology forbids this.'
        else:
            return self.cell_amount - other.cell_amount

    def __mul__(self, other):
        return self.cell_amount * other.cell_amount

    def __truediv__(self, other):
        return self.cell_amount // other.cell_amount

    def make_order(self):
        for i in range(self.cell_amount // self.cell_row):
            self.line += f'{"*" * self.cell_row}\n'
        self.line += f'{"*" * (self.cell_amount % self.cell_row)}\n'
        return self.line


cell_1 = Cell(15, 5)
cell_2 = Cell(13, 6)


print(f'Клетка №1:\n{cell_1.make_order()}')
print(f'Клетка №2:\n{cell_2.make_order()}')
print(f'Сумма клеток 1 и 2: {cell_1 + cell_2}')
print(f'Разность клеток 1 и 2: {cell_1 - cell_2}')
print(f'Произвеедение клеток 1 и 2: {cell_1 * cell_2}')
print(f'Результат деления клеток 1 и 2 (нет не такое деление): {cell_1 / cell_2}')
