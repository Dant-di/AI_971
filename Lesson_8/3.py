# Task 3
class ErrMac(Exception):
    def __init__(self, message):
        self.message = message


step = ''
my_list = []
while step != 'stop':
    step = input('Input the list element - ')
    try:
        if step == 'stop':
            raise ErrMac('Script is finished')
        elif not step.isdigit():
            raise ErrMac('It was not a digit')
    except ErrMac as error:
        print(error)
    else:
        my_list.append(int(step))
print(my_list)
