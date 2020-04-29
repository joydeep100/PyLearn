'''Given a string '000000', we have to find in how many iterations it reaches the target.
condition: we can make value as 1, and all the RHS elements will switch values
Return the number fo steps.
ex. 0100

step - 1 0011
step - 2 0100'''

temp_list = []

def switch(i):
    global temp_list
    if temp_list[i] == '0':
        temp_list[i] = '1'
    else:
        temp_list[i] = '0'

def theFinalProblem(target):
	'''handling this is reverse order, the number of steps required to come to a set of 0's'''
	global temp_list
	target_list = list(target)
	l = len(target_list)

	temp_list = target_list

	final_list_state = ['{}'.format(i) for i in range(l)]
	# backtrack to the original state of '0's...


	count=0

	for i in range(l):
	    if temp_list == final_list_state:
	        break
	    if target_list[i] == '1':
	        count+=1
	        temp_list[i]='0'
	        for j in range(i+1,l):
	            switch(j)

	return(count)

print(theFinalProblem('0100'))