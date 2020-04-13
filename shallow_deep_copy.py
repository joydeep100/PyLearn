#Regular copy - The object is same, but various names are mapped to the same object.

l1=[1,2,3]
l2=l1
l1[0]=9

print(l1,id(l1))
print(l2,id(l2))

# O/P 
# [9, 2, 3] 1966853546632
# [9, 2, 3] 1966853546632

#Shallow copy - Creates a new object, so id's are different but it is only 1 level deep. 
# Any nested items are still using a same reference.
import copy

l3=[[1,2,3],[4,5,6],[7,8,9]]
l4 = copy.copy(l3)
l3[0]=['a','b','c']

print(l3)
print(l4)

# O/P
# [['a', 'b', 'c'], [4, 5, 6], [7, 8, 9]]
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#Deep copy
l4[2][0]=(77)
print(l3)
print(l4)
# O/P
# [['a', 'b', 'c'], [4, 5, 6], [77, 8, 9]]
# [[1, 2, 3], [4, 5, 6], [77, 8, 9]]

# To avoid this we can use...
l5=copy.deepcopy(l3)
l3[2][1]=88

print(l3)
print(l5)
# O/P
# [['a', 'b', 'c'], [4, 5, 6], [77, 88, 9]]
# [['a', 'b', 'c'], [4, 5, 6], [77, 8, 9]]