#generator expression
print((i for i in range(5)))
# O/P <generator object <genexpr> at 0x000001CE6C07A390>

print(list((i for i in range(5))))
# O/P [0, 1, 2, 3, 4]

for i in (i*i for i in range(5)):
	print(i,end=' ')
	
# O/P 0 1 4 9 16


