'''
Find the max difference in an array
'''

def max_difference(arr):
	l = len(arr)
	max_diff = arr[1] - arr[0] # or 0 also would work

	for i in range(0,l):
		for j in range(i+1,l):
			if arr[j] - arr[i] > max_diff:
				max_diff = arr[j] - arr[i]

	return max_diff

arr = [21, 2, 90, 10, 110, 200]
print(f'Max diff. is {max_difference(arr)}')
# O(n^2) since 2 loops are involved

#Efficient approach using 1 loop - O(n)

def max_difference_opt(arr):
	l = len(arr)

	max_diff = arr[1] - arr[0]
	min_val = arr[0]

	for i in range(l):
		if arr[i] - min_val > max_diff:
			max_diff = arr[i] - min_val

		if min_val < arr[i]:
			min_val = arr[i]

	return max_diff

print(f'Max diff. is {max_difference(arr)}')