# Task 5

class Stationery:
    def __init__(self, title='что-то прекрасное'):
        self.title = title

    def draw(self):
        print(f'Создаем {self.title}')


class Pen(Stationery):
    def draw(self):
        print(f'Пишем ручкой {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Чертим карандашом {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'Малюем маркером {self.title}')

gen = Stationery()
gel_pen = Pen()
hard_pencil = Pencil()
black_marker = Handle()

gen.draw()
gel_pen.draw()
hard_pencil.draw()
black_marker.draw()
