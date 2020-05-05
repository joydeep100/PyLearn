'''
Input n,m
Output n*1, n*2 .... n*m
'''
l = []

def fun(start,end,k=1):

	if k > end:
		return
		
	l.append(start*k)
	return fun(start,end,k+1)

fun(2,4)
print(l)