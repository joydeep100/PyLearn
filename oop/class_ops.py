class ComplexNumber:
	def __init__(self,r = 0,i = 0):
		self.real = r
		self.imag = i

	def getData(self):
		print("{0}+{1}j".format(self.real,self.imag))

c1 = ComplexNumber(2,3)
c1.getData()

#deleting an attribute 
# del c1.imag
# c1.getData()
# O/P 
# AttributeError: 'ComplexNumber' object has no attribute 'imag'

#***deleting methods***

# del ComplexNumber.getData	#***Make sure you use class_name.method_name without ()***
# c1.getData()
# O/P 
# AttributeError: 'ComplexNumber' object has no attribute 'getData'

#deleting the object 
# del c1
# print(c1)
# O/P
# AttributeError: 'ComplexNumber' object has no attribute 'getData'