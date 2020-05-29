# list <-> tuple
def packing(*args):
	print(args)

def unpack(a,b,c,d):
	print(a,b,c,d)


packing(1,2,3,4,5)
unpack(*[1,2,3,4])

# named arguments <-> dictionary
def packing_dict(**args):
	print(args)

def unpack_dict(a,b,c):
	print(a,b,c)

packing_dict(a=1,b='strong',c=3)	#Named arguments
unpack_dict(**{'a':1,'b':2,'c':3})

