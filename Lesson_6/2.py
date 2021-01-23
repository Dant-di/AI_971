# Task 2

class Road:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def mass(self):
        amount = self.__length * self.__width * 25 * 5
        return f'Количество асфальта для дороги длинной {self.__length} м, шириной {self.__width} м и толщиной 5 см, ' \
               f'при норме расхода на один квадратный метр равно {round(amount / 1000)} т '


lngt = int(input('Введите длинну дороги в метрах - '))
wdth = int(input('Введите ширину дороги в метрах - '))
asphalt = Road(lngt, wdth)
print(asphalt.mass())
