# Task 5

stop = False
tot_sum = 0


def get_data():
    global inp
    inp = input('Введите несколько чисел, разделенных пробелами - ').split()
    return inp


def str_chck():
    global stop
    global tmp_str
    tmp_str = []
    for el in inp:
        if el.isdigit():
            tmp_str.append(el)
        else:
            stop = True
    return tmp_str, stop


def inter_sum():
    x = 0
    for el in tmp_str:
        x = x + int(''.join(el))
    return x


while True:
    get_data()
    str_chck()
    inter_sum()
    temp_str, stop = str_chck()
   
    tot_sum = tot_sum + inter_sum()
    print(tot_sum)
    if stop is True:
        break

print('Program terminated violently. >:-]')
