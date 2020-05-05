m=2
n=4

k=1
o=n+1
def fun(m,n):
	global k,o;

	while k!=o:
		print(m*k)
		k=k+1
		fun(m,k)


# fun(m,n)


def fun2(start,end,k=1):
	# import pdb;pdb.set_trace()
	while(k!=end):
		fun2(start,end,k+1)
	print(m*k)


fun2(2,4)