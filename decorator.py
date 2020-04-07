def decorator_func(func):

	def inner_func():
		a = str(func())
		b=a+' nononon'
		return b

	return inner_func

@decorator_func
def orig_func():
	return 'hello'

#This is one method, if we use this then @ in #10 is not needed
#orig_func = decorator_func(orig_func)

# or - This is same as #15 code, only thing is it needs the extra code in line #8
print(orig_func())