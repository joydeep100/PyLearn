def func(arg):

	def function(arg1):
		a = arg 
		b = arg + arg1
		c = arg + arg1 + 1
		return c

	return function

x = func(10)
print(x(20))

#o/p 31

#ex-2

def func1():

	def func2():
		return 'hello'

	return func2

fun = func1()
print(fun())