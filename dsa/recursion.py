m=2
n=3

k=1
o=n+1
def fun(m,n):
	global k,o;

	if k==o:
		return

	print(m*k)
	k=k+1
	return fun(m,k)


fun(m,n)

