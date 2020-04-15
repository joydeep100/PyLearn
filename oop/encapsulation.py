class Encap:

	# use __ as prefix for attribute and methods to make it private 
	# and only class methods can access / modify it.

	__private_var = 'pv'

	def __init__(self):
		pass

	def get_private_vars(self):
		return self.__private_var

	def __private_method(self):
		return 'I am a private method'

	def show_private_method(self):
		print(self.__private_method())

o = Encap()

# Private attribute
# o.__pricave_var		# or print(Encap.__private_var)
# O/P
# AttributeError: 'Encap' object has no attribute '__pricave_var'

print(o.get_private_vars())
#O/P pv   -- works

#Private method
# o.__private_method()
# O/P
# AttributeError: 'Encap' object has no attribute '__private_method'

o.show_private_method()
# O/P
# I am a private method' -- works