''''
Ex. string 'abba'
The list of all anagrammatic pairs are [a,a],[b,b],[ab,ba],[abb,bba]
'''
from collections import Counter

def sherlockAndAnagrams(s):
	l=len(s)
	pairs=0

	for i in range(1,l+1):
		slice_list=[]
		tmp_list = []

		for j in range(l-(i-1)):
			slice_list.append(s[j:j+i])

		for item in slice_list:
			tmp_list.append(''.join(sorted(item)))

		hash_map = Counter(tmp_list)

		for value in hash_map.values():
			if value >= 2:
				pairs+=value*(value-1)//2	
				#Got n(n-1)/2 from discussion board, and seemed to perfectly fit in
				#Combinations logic :D

	return(pairs)

print(sherlockAndAnagrams('kkkk'))
