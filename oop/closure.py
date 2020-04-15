# A Closure is a function object that remembers values in 
# enclosing scopes even if they are not present in memory.
def func(arg):

	def function(arg1):
		a = arg 	# This arg is from the enclosing scope.
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