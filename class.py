class newClass(object):
# in #1 object keyword is not needed.

	#This is a class variable
	MACRO = 1


	#The variables defined under self is the class variable
	def __init__(self,name,no):
		self.name = name
		self.no = no

	#When these methods are called from outside it translates the code into 
	# className.methodName(instanceName), which is the reference self needs
	def print_stuff(self):
		print('name is {} and no is {}.'.format(self.name,self.no))

obj = newClass('Joydeep',123)
# object creation is always like this.

obj.print_stuff()
newClass.print_stuff(obj)
# calling can be either one of the above ways

# obj.print_stuff()
# newClass.MACRO = 2
# print(obj.MACRO,obj.name)