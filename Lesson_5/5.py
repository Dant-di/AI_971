# Task 5
from random import randint as ri, random as rd

with open('my_file_5.txt', 'w', encoding='UTF8') as f:
    list = [rd()*100 for el in range(1, ri(10, 100))]
    f.writelines(' '.join(map(str, list)))

with open('my_file_5.txt', 'r', encoding='UTF8') as f_2:
    print(f'The sum of all numbers in the file "{f.name}" is: {round(sum([float(el) for el in f_2.read().split()]), 2)}')


# А теперь читы!!!
with open('my_file_5_cheat.txt', 'w', encoding='UTF8') as f:
    list2 = [ri(-50, 100) for el in range(1, ri(10, 100))]
    f.writelines(' '.join(map(str, list2)))
    f.write('\n' + f'The sum of all the numbers above in the file is: {sum(list2)}')
    print(f'The sum of all the numbers in the file "{f.name}" is: {sum(list2)}')
