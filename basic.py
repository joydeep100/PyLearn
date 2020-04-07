#Converting a list back to string.
string = "abracadabra"
l = list(string)
l[5] = 'k'
string = ''.join(l)


#Replace
'Hello world'.replace('l','z')
#O/P 'Hezzo worzd'

#Sorted <object>.sort() changes the original string, but sorted is like an filter that is applied over
min = sorted(list(set([i[1] for i in scores_list])))[1]
