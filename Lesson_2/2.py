# Task 2
my_list = []
while True:
    b = input('Введите элементы списка. Для завершения ввода наберите "end" - ')

    if b != 'end':
        my_list.append(b)
    else:
        break

if len(my_list) % 2 == 0:
    for i in range(0, len(my_list), 2):
        my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
else:
    for i in range(0, len(my_list)-1, 2):
        my_list[i], my_list[i+1] = my_list[i+1], my_list[i]

print(f'Current list - {my_list}')