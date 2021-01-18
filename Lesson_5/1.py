# Task 1

with open('my_file_1.txt', 'w') as res:
    inpt = ' '
    while inpt != '':
        inpt = input('Enter the data. For exit simply press "Enter". ')
        res.write(inpt + '\n')


