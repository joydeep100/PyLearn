str = 'abracadabra'

print(any(c.isalnum() for c in str))
print(any(c.isalpha() for c in str))
print(any(c.isdigit() for c in str))
print(any(c.islower() for c in str))
print(any(c.isupper() for c in str))

#returns True or False

print(all(i for i in range(1,10) if i==1 or i == 2))

#O/P True