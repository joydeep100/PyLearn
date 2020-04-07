def func1(func_arg):
	print(func_arg())


def func2():
	return 'hello'


func1(func2)