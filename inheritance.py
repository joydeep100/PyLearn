class A:

	M1 = 10;

	def func1(self):
		print('A')


	def func2(self):
		print('B')

class B(A):

	#M1 = 20;

	def func3(self):
		print('C',super().M1)		#super for variables
		super().func1()				#as well as methods
		# internally translates to A.func1(self)


	def func4(self):
		print('D')		


o = B()
o.func3()