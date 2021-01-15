# Task 1
from sys import argv

"""
When running the script from the terminal/command prompt please supply following parameters after the file name
    hours - any float number, defines the amount of hours employee has worked
    rate - any float number, defines the hourly rate of employee
    bonus - any float number, defines bonus in percent
    
    example of the script launch in terminal:
        python 1.py 200 25 10
    where "1.py" is the file name, "200" amount of hours worked, "25" hourly rate and "10" is a 10% bonus
    ***Please note that bonus is calculated only if the minimum required amount of hours of 176 were worked***
"""

file_name, hours, rate, bonus = argv
hours, rate, bonus = float(hours), float(rate), float(bonus)

if hours > 248:
    print("It's hardly possible to work like this. I will see you manager.")

elif hours >= 176:
    pay = (hours * rate) + (hours * rate) * bonus/100
    print(f'Well done! You have earned additional bonus and your payout this month is - {pay} ({hours * rate} salary '
          f'and {pay - hours * rate} bonus)')

else:
    pay = (hours * rate)
    print(f'No bonus for you, try harder next time! Your payout this month is - {pay}')
