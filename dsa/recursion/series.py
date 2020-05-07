'''
Input n,m
Output n*1, n*2 .... n*m
'''
l = []

def fun(m,k=1):

	if k > n:
		return
		
	l.append(m*k)
	
	return fun(m,k+1)

m,n = 2,6
fun(m)
print(l)