# A Closure is a function object that remembers values in 
# enclosing scopes even if they are not present in memory.
def func(arg):

	def function(nested_arg):
		return arg + nested_arg # here 'arg' is from the enclosing scope.

	return function

x = func(10)
print(x(20))

#o/p 31