# Task 4

import random


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} is moving')

    def stop(self):
        print(F'{self.name} has stopped')

    def turn(self):
        print(f"{self.name} turned {random.choice(['left', 'right', 'back'])}")

    def show_speed(self):
        return f'Current {self.name} speed is {self.speed}'


class TownCar(Car):
    def show_speed(self):
        message = f'is overspeeding at' if self.speed > 60 else f'current speed is'
        return f'{self.name} {message} {self.speed}'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        message = f'is overspeeding at' if self.speed > 40 else f'current speed is'
        return f'{self.name} {message} {self.speed}'


class PoliceCar(Car):
    pass


_color = random.choice(['Blue', 'Red', 'Green', 'Black', 'Yellow', 'White', 'Grey',  ])

kia = TownCar(random.randint(1, 180), _color, 'Kia Ceed', False)
bugatti = SportCar(random.randint(1, 480), _color, 'Bugatti Chiron', False)
gaz = WorkCar(random.randint(1, 120), _color, 'Gazon', False)
bobik = PoliceCar(random.randint(1, 180), _color, 'Ford Focus', True)

print(f'Car info:\n Car: {kia.color} {kia.name}\n Car current speed: {kia.speed}\n Is it police: {kia.is_police}')
kia.go()
kia.turn()
print(kia.show_speed())
kia.stop()

print(f'\nCar info:\n Car: {bugatti.color} {bugatti.name}\n Car current speed: {bugatti.speed}\n Is it police: '
      f' {bugatti.is_police}')

bugatti.go()
bugatti.turn()
print(bugatti.show_speed())
bugatti.stop()

print(f'\nCar info:\n Car: {gaz.color} {gaz.name}\n Car current speed: {gaz.speed}\n Is it police: {gaz.is_police}')
gaz.go()
gaz.turn()
print(gaz.show_speed())
gaz.stop()

print(f'\nCar info:\n Car: {bobik.color} {bobik.name}\n Car current speed: {bobik.speed}\n Is it police: '
      f'{bobik.is_police}')
bobik.go()
bobik.turn()
print(bobik.show_speed())
bobik.stop()
