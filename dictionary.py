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

#inserting
d3['name']='joy'

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

#Dictionary comprehension
old_price = {'milk': 1.02, 'coffee': 2.5, 'bread': 2.5}
new_price = {item: value*2.5 for (item, value) in old_price.items()}

print(new_price)
# Output {'milk': 0.7752, 'coffee': 1.9, 'bread': 1.9}