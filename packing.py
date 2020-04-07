# list <-> tuple
def unpack(a,b,c,d):
	print(a,b,c,d)


def packing(*args):
	print(type(args))
	print(args)


#unpack(*[1,2,3,4])

#packing(1,2,3,4,5)

# dictionary


def unpack_dict(a,b,c):
	print(a,b,c)

def packing_dict(**args):
	print(type(args))
	print(args)

#unpack_dict(**{'a':1,'b':2,'c':3})

packing_dict(a=1,b='strong',c=3)