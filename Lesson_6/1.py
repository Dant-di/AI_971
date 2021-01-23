# Task 1
import time

class Trafficlight:
    __color = ['red', 'yellow', 'green']

    def running(self, sl1, sl2, sl3):
        print(self.__color[0])
        time.sleep(sl1)
        print(self.__color[1])
        time.sleep(sl2)
        print(self.__color[2])
        time.sleep(sl3)


change = Trafficlight()
i = 0
cnt = int(input('How many times we cycle traffic light? - '))
while i < cnt:
    change.running(7, 2, 5)
    i +=1

