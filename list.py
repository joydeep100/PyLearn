s1='hello'
print(list(s1))
# ['h', 'e', 'l', 'l', 'o']

l1=[1,2]

l1[0]=9
# [9, 2]

#adding
l1.append(10)
# [9,2,10]

l1.insert(3,11)
# [9, 2, 10, 11]

l1.extend([11,12])
# [9, 2, 10, 11, 11 ,12]

#remove
l1.pop()
# [9, 2, 10, 11, 11]

l1.remove(11)
# [9, 2, 10, 11]		#only one items is removed
