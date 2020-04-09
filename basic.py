#//Converting a list back to string.
string = "abracadabra"
l = list(string)
l[5] = 'k'
string = ''.join(l)


#//Replace
'Hello world'.replace('l','z')
#O/P 'Hezzo worzd'

#Sorted <object>.sort() changes the original string, but sorted is like an filter that is applied over
min = sorted(list(set([i[1] for i in scores_list])))[1]

# Justify  - center, ljust & rjust
# >>> 'hello'.center(10,'-')
# '--hello---'
# >>> 'hello'.center(10,'-')
# '--hello---'

#//Working with reverse slicing, A better approach
print([1,2,3,4,5][1:3])
#O/P [2, 3]
print([1,2,3,4,5][1:3][::-1])
#O/P [3, 2]
