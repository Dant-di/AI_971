# Task 6. 

class ErrMac(Exception):
    def __init__(self, message):
        self.message = message


class BuroTechnik:
    common = {'model': '', 'price': ''}

    @staticmethod
    def get_data():
        for f in BuroTechnik.common.keys():
            BuroTechnik.common[f] = input(f'enter the {f} - ')
        return BuroTechnik.common

class Printer(BuroTechnik):
    unique = {'printer type': '', 'max format': ''}

    @staticmethod
    def get_data():
        for f in Printer.unique.keys():
            Printer.unique[f] = input(f'enter the {f} - ')
        return Printer.unique


class Scanner(BuroTechnik):
    unique = {'max format': ''}

    @staticmethod
    def get_data():
        for f in Scanner.unique.keys():
            Scanner.unique[f] = input(f'enter the {f} - ')
        return Scanner.unique


class Calc(BuroTechnik):
    unique = {'max digits': '', 'power': ''}

    @staticmethod
    def get_data():
        for f in Calc.unique.keys():
            Calc.unique[f] = input(f'enter the {f} - ')
        return Calc.unique


class Warehouse:
    sku = {'Scanners': [], 'Printers': [], 'Calculators': []}
    sku_amount = {'Scanners': 0, 'Printers': 0, 'Calculators': 0}
    free_space = 50
    sku_out = []

    @staticmethod
    def inbound():
        print(f"1 - Scanner.\n"
              f"2 - Printer.\n"
              f"3 - Calculator\n"
              f"4 - Cancel.")
        var_inb = int(input("Please select item (type menu number): "))
        if var_inb == 4:
            pass
        elif var_inb == 1:
            temp_dict = {'type': 'Scanner'}
            temp_dict.update(BuroTechnik.get_data())
            temp_dict.update(Scanner.get_data())
            var_1 = int(input('Enter amount - '))
            try:
                if var_1 < 0:
                    raise ErrMac('Amount can not be negative!\n')
            except ErrMac as error:
                print(error)
                menu()
            if var_1 > Warehouse.free_space:
                print('Not enough space in the warehouse. Sorry.\n')
            else:
                Warehouse.sku_amount['Scanners'] += var_1
                Warehouse.sku['Scanners'].append(temp_dict)
                Warehouse.free_space -= var_1

        elif var_inb == 2:
            temp_dict = {'type': 'Printer'}
            temp_dict.update(BuroTechnik.get_data())
            temp_dict.update(Printer.get_data())
            var_1 = int(input('Enter amount - '))
            try:
                if var_1 < 0:
                    raise ErrMac('Amount can not be negative!\n')
            except ErrMac as error:
                print(error)
                menu()
            if var_1 > Warehouse.free_space:
                print('Not enough space in the warehouse. Sorry.\n')
            else:
                Warehouse.sku_amount['Printers'] += var_1
                Warehouse.sku['Printers'].append(temp_dict)
                Warehouse.free_space -= var_1
        elif var_inb == 3:
            temp_dict = {'type': 'Calculator'}
            temp_dict.update(BuroTechnik.get_data())
            temp_dict.update(Calc.get_data())
            var_1 = int(input('Enter amount - '))
            try:
                if var_1 < 0:
                    raise ErrMac('Amount can not be negative!\n')
            except ErrMac as error:
                print(error)
                menu()
            if var_1 > Warehouse.free_space:
                print('Not enough space in the warehouse. Sorry.\n')
            else:
                Warehouse.sku_amount['Calculators'] += var_1
                Warehouse.sku['Calculators'].append(temp_dict)
                Warehouse.free_space -= var_1
        else:
            print("Wrong input. Try again.\n")

    @staticmethod
    def outbound():
        if sum(Warehouse.sku_amount.values()) == 0:
            print('Warehouse is empty.')
        else:
            cnt = 0
            for key in Warehouse.sku_amount:
                cnt += 1
                print(f'{cnt} - {key}: {Warehouse.sku_amount.get(key)}')
            print(f"4 - Cancel.")
            var_out = int(input("Please select what to move (type menu number): "))
            if var_out == 4:
                pass
            elif var_out == 1:
                amount = int(input('Enter the amount of scanners - '))
                try:
                    if amount < 0:
                        raise ErrMac('Amount can not be negative!')
                except ErrMac as error:
                    print(error)
                    menu()
                if amount > Warehouse.sku_amount.get('Scanners'):
                    print('Sorry, there are not enough units.')
                else:
                    dept = input('Enter the department name - ')
                    Warehouse.sku_amount['Scanners'] -= amount
                    Warehouse.free_space += amount
                    Warehouse.sku_out.append({'Name': 'Scanner', 'Amount': amount, 'Department': dept})
            elif var_out == 2:
                amount = int(input('Enter the amount of printers - '))
                try:
                    if amount < 0:
                        raise ErrMac('Amount can not be negative!')
                except ErrMac as error:
                    print(error)
                    menu()
                if amount > Warehouse.sku_amount.get('Printers'):
                    print('Sorry, there are not enough units.')
                else:
                    dept = input('Enter the department name - ')
                    Warehouse.sku_amount['Printers'] -= amount
                    Warehouse.free_space += amount
                    Warehouse.sku_out.append({'Name': 'Printer', 'Amount': amount, 'Department': dept})
            elif var_out == 3:
                amount = int(input('Enter the amount of scanners - '))
                try:
                    if amount < 0:
                        raise ErrMac('Amount can not be negative!')
                except ErrMac as error:
                    print(error)
                    menu()
                if amount > Warehouse.sku_amount.get('Calculators'):
                    print('Sorry, there are not enough units.')
                else:
                    dept = input('Enter the department name - ')
                    Warehouse.sku_amount['Calculators'] -= amount
                    Warehouse.free_space += amount
                    Warehouse.sku_out.append({'Name': 'Calculator', 'Amount': amount, 'Department': dept})
            else:
                print("Wrong input. Try again.")


def menu():
    while True:
        print(f"1 - Add item to storage.\n"
              f"2 - Transfer it to department.\n"
              f"3 - Display what's in the warehouse\n"
              f"4 - Display how much space left in warehouse\n"
              f"5 - Exit.")
        var = int(input("Please select what to do (type menu number): "))
        if var == 5:
            break
        elif var == 1:
            Warehouse.inbound()
        elif var == 2:
            Warehouse.outbound()
        elif var == 3:
            print('Currently in the warehouse:')
            for key in Warehouse.sku_amount:
                print(f'{key}: {Warehouse.sku_amount.get(key)}')
        elif var == 4:
            print(f'There are {Warehouse.free_space} places left.\n')
        else:
            print("Wrong input. Try again.")


menu()
