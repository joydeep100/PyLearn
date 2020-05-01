'''find the biggest repeating sub string from the given string'''
str='hithisisgooglegoogl'

l = len(str)

ss_count = 0
ss_str = ''
'''this algorithm can be reverese, meaning to start from the biggest substring and if the count 
becomes more than the lenght of the currecnt iteration of sub string, we can break'''
for i in range(2,l+1):

	for j in range(l-i+1):

		str_slice = str[j:j+i]
		str_slice_count = str.count(str_slice)

		if str_slice_count >= ss_count and len(str_slice) >= len(ss_str):
			ss_count = str_slice_count
			ss_str = str_slice

print(f'String with max repeats is :{ss_str} with:{ss_count} repeats')


