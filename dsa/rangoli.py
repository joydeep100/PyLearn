import string
alpha = string.ascii_lowercase
n = int(input())

s=[]
for i in range(n):
	p=('-'.join(alpha[i+1:n][::-1] + alpha[i:n])).center(4*n-3,'-')
	s.append(p)

print('\n'.join(s[::-1] + s[1:n]))

# O/P
# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------

