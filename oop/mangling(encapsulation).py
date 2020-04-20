class A:
	__b = 10

o = A()
# print(o.__b)
# O/P AttributeError: 'A' object has no attribute '__b'

print(o._A__b)
# O/P 10
o._A__b = 20

print(o._A__b)
# O/P 20

# When __ is used, Python interpreter rewrites the attribute name
# in order to avoid naming conflicts in subclasses. This is called mangling.
# Still there is no protection deliberable, but implicit protection is there.
# If you need protection(Encapsulation) then we need to implement @property