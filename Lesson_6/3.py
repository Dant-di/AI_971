# Task 3

class Worker:
    def __init__(self, name, second_name, surname, position, wage, bonus):
        self.name = name
        self.second_name = second_name
        self.surname = surname
        self. position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        print(f'{self.name} {self.second_name} {self.surname}, {self.position}')

    def get_total_income(self):
        print(sum(self._income.values()))


employee = Position('Иван', 'Федорович', 'Крузенштерн','Человек и пароход', 250000, 15000)
employee.get_full_name()
employee.get_total_income()


# with input method
# fio = input('Введите ФИО - ').split()
# fin = input('Введите оклад и премию через пробел - ').split()
# _position = input('Введите должность - ')
#
# employee = Position(fio[1], fio[2], fio[0], _position, float(fin[0]), float(fin[1]))
# employee.get_full_name()
# employee.get_total_income()
