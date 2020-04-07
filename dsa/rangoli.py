import string
alpha = string.ascii_lowercase

n = 5
L = []
for i in range(n):
    s = "-".join(alpha[i:n])
    print(s)
    L.append((s[::-1]+s[1:]).center(4*n-3, "-"))

print('\n'.join(L[:1:-1] + L))

# O/P
# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------

