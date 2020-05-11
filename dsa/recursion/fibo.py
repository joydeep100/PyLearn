def fibo(n):
	if n == 0 or n == 1:
		return n
	else:
		return fibo(n-1) + fibo(n-2) 

D={}
def fiboUsingDP(n):
	if n == 0 or n ==1:
		return n

	elif n in D.keys():
		return D[n]
	
	else:
		result = fiboUsingDP(n-1) + fiboUsingDP(n-2)
		D[n]=result		#Caching all intermediate results (Dynamic Programming)
		return result

n=40
# print(fibo(n))
print(fiboUsingDP(n))