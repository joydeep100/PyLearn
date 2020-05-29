num = 12345
l = 5

m=10
n=1

for i in range(l):
    print(num%m//n)
    num=num-(num%m)
    m=m*10
    n=n*10
