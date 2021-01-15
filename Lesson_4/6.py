# Task 6

from itertools import count, cycle


for i in count(3):
    if i > 10:
        break
    else:
        print(i)

my_list = ['Old', 'McDonald', 'Had', 'a', 'farm']
c = 0
for el in cycle(my_list):
    if c == 5:
        break
    else:
        print(el)
        if el == 'farm':
            c += 1
