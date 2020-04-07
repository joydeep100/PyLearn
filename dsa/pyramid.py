def right_pymd(n):
	for i in range(n):
		for i in range(i+1):
			print('*',end='')
		print('\n')

#right_pymd(5)

def left_pymd(n):

	for i in range(n):

		for j in range(n-i):
			print(' ',end='')

		for k in range(i+1):
			print('*',end='')

		print('\n')

#left_pymd(5)

def full_pymd(n):
	l=1
	for i in range(n):

		for j in range(n-i):
			print(' ',end='')

		for k in range(i+l):
			print('*',end='')

		print('\n')
		l+=1

n=5
full_pymd(n)

#For - full pyramid - using list comprehension
pattern = [('*'*(2*i+1)).center(2*n,' ') for i in range(n)]
print('\n'.join(pattern))