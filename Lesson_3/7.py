# Task 7, option 1
def int_func(a):
	return a.capitalize()


def str_cap(str1):
	var = ()
	str2 = ''
	str1 = str1.split()
	for el in str1:
		el = (int_func(el),)
		var = var + el
		str2 = ' '.join(var)
	return str2


wrd = input('Введите несколько слов латиницей с маленькой буквы, разделенные пробелами - ')

print(str_cap(wrd))


# ----------------------------------------------------------------------------------------------------------------------
# Task 7, option 2 - easy solution with one function

def int_func1(x):
	x = x.title()
	return x


a = input('Введите несколько слов латиницей с маленькой буквы, разделенные пробелами - ')
print(int_func1(a))

# ----------------------------------------------------------------------------------------------------------------------
# Task 7, option 3 to take care of special characters

def int_func2(a):
	var = ()
	a = (a).split()
	for i in a:
		i = ((i.capitalize()),)
		var = var + i
		str1 = ' '.join(var)
	return str1


z = input('Введите несколько слов латиницей с маленькой буквы, разделенные пробелами - ')
print(int_func2(z))
