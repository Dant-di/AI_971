# Task 3
from statistics import mean

names = []
sal = []
with open('my_file_3.txt', 'r', encoding='UTF8') as f:
    for line in f:
        line = line.split()
        names.append(line[0])
        sal.append(float(line[1]))
    dict = {key: value for key, value in zip(names, sal)}
    low_sal = [keys for keys in dict if dict.get(keys) < 20000]
    print(f"Following employees have salary less than 20 K: {', '.join(low_sal)}.")
    print(f'Average salary of all {len(dict.keys())} employees is {round(mean(dict.values()), 2)}.')
