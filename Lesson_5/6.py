# Task 6
import re

keys = []
values = []
with open('my_file_6.txt', 'r', encoding='UTF8') as f:
    for el in f.readlines():
        _key = ''.join(el.split(sep=':').pop(0))
        keys.append(_key)
        line2 = re.findall(r'\d+', el)
        val = 0
        for elem in line2:
            val += int(elem)
        values.append(val)
    dict = {key: value for key, value in zip(keys, values)}
    print(dict)
