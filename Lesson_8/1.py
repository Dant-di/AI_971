# Task 1

class Date:
    def __init__(self, inpt):
        self.inpt = inpt

    @classmethod
    def convert(cls, param):
        date = []
        for i in param.split(sep="-"):
            date.append(int(i))
        return date

    @staticmethod
    def validate(date):
        month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                 'November', 'December']
        leap_year = ''
        if date[2] % 400 == 0 and date[2] % 100 == 0:
            leap_year = 'yes'
        elif date[2] % 100 == 0 and date[2] % 400 != 0:
            leap_year = 'no'
        elif date[2] % 4 == 0:
            leap_year = 'yes'
        else:
            leap_year = 'no'

        if date[1] < 1 or date[1] > 12:
            return 'Month can be a integer from 1 to 12'
        elif date[0] < 1:
            return "Day of month can't be less than 1"
        elif date[1] in [1, 3, 5, 7, 8, 10, 12] and date[0] > 31:
            return f'{month[date[1]-1]} has max 31 days'
        elif date[1] in [4, 6, 9, 11] and date[0] > 30:
            return f'{month[date[1]-1]} has max 30 days'
        elif date[1] == 2 and leap_year == 'yes' and date[0] > 29:
            return 'February in leap year have max 29 days'
        elif date[1] == 2 and leap_year == 'no' and date[0] > 28:
            return 'February in non leap year has max 28 days'
        if date[2] < 1:
            return 'Our year is not a list -  count starts from 1, not from 0'
        else:
            return 'Date is correct'

the_day = '30-04-2021'
obj = Date(the_day)
print(Date.convert(the_day))
print(obj.validate(Date.convert(the_day)))
