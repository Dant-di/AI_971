# Taks 2

from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def calc(self):
        pass


class Coat(Clothes):

    def __init__(self, var):
        self.var = var

    @property
    def calc(self):
        return self.var / 6.5 + 0.5


class Suit(Clothes):

    def __init__(self, var):
        self.var = var

    @property
    def calc(self):
        return self.var * 2 + 0.3


a = Coat(52)
b = Suit(185)
print(f'На пальто и костюм потребуется {a.calc + b.calc} метров (!) ткани')
