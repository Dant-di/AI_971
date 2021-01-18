# Task 7
"""For this example integer values of revenues and costs used"""
from statistics import mean
import json

firms = []
income = []

with open('my_file_7.txt', 'r', encoding='UTF8') as f:
    for line in f:
        line = line.split(sep='   ')
        firms.append(line[0])
        income.append(int(line[2]) - int(line[3]))
    avg_data = [inc_val for inc_val in income if inc_val >= 0]
    avg_profit = {'average_profit': mean(avg_data)}
    fin_list =[{key: value for key, value in zip(firms, income)}, avg_profit]

with open('my_file_7.json', 'w', encoding='UTF8',) as f_j:
    json.dump(fin_list, f_j, ensure_ascii=False)
