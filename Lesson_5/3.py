# Task 3
from statistics import mean

def f_len(): #Define file length
    with open(name, 'r', encoding='UTF8') as a:
        a.read()
        end = a.tell()
        a.seek(0)
        return end


with open('my_file_3.txt', 'r', encoding='UTF8') as f:
    stop = 0
    name = f.name
    new_list = []
    while stop < f_len():
        list = tuple(f.readline().split())
        new_list.append(list)
        stop = f.tell()
    dict = {key: float(value) for key, value in new_list}
    low_sal = [keys for keys in dict if dict.get(keys) < 20000]
    print(f"Following employees have salary less than 20 K: {', '.join(low_sal)}.")
    print(f'Average salary of all {len(dict.keys())} employees is {round(mean(dict.values()), 2)}.')
