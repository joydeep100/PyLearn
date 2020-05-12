def mergeIntervals(arr):

	i=1
	s_arr = sorted(arr)

	while(i < len(s_arr)):	#for dynamically updating list

		if s_arr[i][0] in range(s_arr[i-1][0],s_arr[i-1][1]+1):
			s_arr[i-1][0]=min(s_arr[i-1][0],s_arr[i][0])
			s_arr[i-1][1]=max(s_arr[i-1][1],s_arr[i][1])
			s_arr.pop(i)
		else:
			i+=1

	print(s_arr)

arr = [[1,2`],[2,6],[8,10],[15,18]]
mergeIntervals(arr) 
# o/p [[1, 6], [8, 10], [15, 18]]