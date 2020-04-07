#Takes a cmd as a string and executes inside the Python shell
# x = 1
# print(eval('x + 1'))		#ex-1
N = int(input())

cmd_list = []
list=[]

for i in range(N):
    cmd_list.append(input().strip())

for i in range(N):
	cmd,*args=cmd_list[i].split()

	if (cmd=='print'):
		print(list)

	else:	
		arg='(' + ','.join(args) + ')'
		cmd=cmd+arg
		eval('list.'+cmd)	#eval used here also. ex-2 in a slightly diff manner
