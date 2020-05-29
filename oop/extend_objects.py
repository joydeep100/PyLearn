'''How to add functionality to an existing object by inheritance'''

from collections import Counter

# Built-in namespace
import builtins

class eList(list):

	def duplicate(self):
		return [key for key,val in (Counter(self)).items() if val >=2]


builtins.list = eList

print(list('abracadasjdbj').duplicate())		#vanilla syntax, we cannot use l = [1,2,3]; l.duplicates()