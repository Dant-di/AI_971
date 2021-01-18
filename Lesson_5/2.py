# Task 2
with open('my_file_2.txt', 'r') as f:
    i = 0
    for el in f:
        line = el.split()
        i += 1
        print(f'In the string {i} there are {len(line)} words')

    print(f'There total {i} strings.')

