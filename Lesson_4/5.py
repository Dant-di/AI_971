# Task 5
from functools import reduce

new_list = [el for el in range(100, 1001) if el % 2 == 0]
print(new_list)


def my_func(el_1, el_2):
    return el_1 * el_2


print(reduce(my_func, new_list))
