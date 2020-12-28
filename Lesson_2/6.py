# Task 6
goods = []
i = 0

while True:
    print('1. Ввод данных\n2. Аналитика\n3. Выход')
    inp = input('Выберите пункт меню - ')

    if inp == '1':
        data = input('Введите через запятую характеристики товара: название, цена, количество, единица измерения - ').split(',')
        tup = [i+1, {'название': data[0], 'цена': data[1], 'кол-во': data[2], 'ед. изм': data[3]}]
        goods.append(tuple(tup))

        i += 1
    elif inp == '2':
        val = list(goods[0][1].keys())
        out = {val[0]: list({goods[0][1].get(val[0]), goods[1][1].get(val[0]), goods[2][1].get(val[0])}),
               val[1]: list({goods[0][1].get(val[1]), goods[1][1].get(val[1]), goods[2][1].get(val[1])}),
               val[2]: list({goods[0][1].get(val[2]), goods[1][1].get(val[2]), goods[2][1].get(val[2])}),
               val[3]: list({goods[0][1].get(val[3]), goods[1][1].get(val[3]), goods[2][1].get(val[3])})}
        print(out)
    elif inp == '3':
        break

    else:
        print('Введите заново')
