# Task 5
my_list = [10, 9, 7, 6, 3, 2]

a = int(input('Введите рейтинг (натуральное число) - '))
if a in my_list:

    my_list.insert(my_list.index(a)+1, a)
    print(my_list)
else:
    if a < my_list[-1]:
        my_list.append(a)
    for el in my_list:
        if a > el:
            my_list.insert(my_list.index(el), a)
            break
        else:
            continue
    print(my_list)
