from collections import Counter

s='dsakh jsakdh jdashd shdslahdq ljlajd ldjalsjd ljwlqke dasdnjkas'.split()

c=Counter(s)

print(c)
# o/p Counter({'dsakh': 1, 'jsakdh': 1, 'jdashd': 1, 'shdslahdq': 1, 'ljlajd': 1, 'ldjalsjd': 1, 'ljwlqke': 1, 'dasdnjkas': 1})
# this is exactly like a dict