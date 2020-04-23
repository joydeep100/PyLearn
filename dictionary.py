#creating
d1 = {'name':'joy','age':20}
d2 = dict(name='joy',age=20)

# {'name': 'joy', 'age': 20}

#tip
print('age' in d2)
# True

#nested
d3 = {'employees':{'Dave':{'id':100,'role':'associate'},'Ava':{'id':200,'role':'hr'}}}

print(d3['employees']['Ava']['id'])
# 200

#updating
d3['employees']['Ava']['id']=201
print(d3['employees']['Ava']['id'])
# 201

d3['employees']['John']={'id':300,'role':'cto'}
print(d3['employees']['John'])
# {'id': 300, 'role': 'cto'}

#accessing
for i in d3['employees']:		# no need to explicitly mention keys()
	print(i)

for i in d3['employees'].values():
	print(i)

for i,j in d3['employees'].items():
	print(i,j)

#deleting
d5 = {'a':1 , 'b':2, 'c':3}
d5.pop('a')	#pops a specific key
print(d5)
# o/p {'b': 2, 'c': 3}

d5.popitem()	#pops last item

del d5['b'] #same as pop(<key>)
print(d5) 