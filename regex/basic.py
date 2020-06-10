import re

#starts with(^) a, ends with($) e, period = single character (except newline char '\n')
print(re.match('^a...e$','abcde'))

#starts with ab
print(re.match('^ab','abcde'))

#starts with ab
print(re.match('...de$','abcde'))
print(re.match('de$','abcde'))		#This does not match!!

#starts with a, ends with 5, length = 5
print(re.match('[abcde]','abcde'))
print(re.match('[a-e]','abcde'))
print(re.match('[1-5]','12345'))

#inverted 
print(re.match('[^a-z]','12345'))

# * , 0 or more occurances of the pattern in the parenthesis
# + , 1 or more occurances of the pattern in the parenthesis
# ? , 0 or 1 occurances of the pattern in the parenthesis
print(re.match('bat(wo)*man','batman'))
print(re.match('bat(wo)*man','batwoman'))


print(re.match('bat(wo)+man','batman'))	# this will not match
print(re.match('bat(wo)+man','batwoman'))

print(re.match('bat(wo)?man','batman'))
print(re.match('bat(wo)?man','batwoman'))

# string{m,n}, string matches min m times, max n times
print(re.match('a{2}','aa'))
print(re.match('a{2,4}','aa'))
print(re.match('a{2,4}','aaaaaaaaa'))	#sub strings :: aa, aaa, aaaa (OR operation)

print(re.match('bat(wo){1,3}man','batwowowoman'))


#match atleast 1 char from [], if possible try upto 2
print(re.match('[a-e]{1,2}','axxxx'))
print(re.match('[a-e]{1,2}','abxxx'))
print(re.match('[a-e]{1,2}','aexxx'))
print(re.match('[a-e]{1,3}','abxxx'))	#'ab' is matched!

# Alteration - OR
print(re.match('a|e','aaa'))

# \ is escape character

# Findall is cool! trying ipv4 regex (No perfect at all :)
print(re.findall('[1-9][0-5]*[0-5]*.[0-2][0-5]*[0-5]*.[0-2][0-5]*[0-5]*.[0-2]*[0-5]*[0-5]','2.225.215.205'))
# O/P ['255.225.215.205']

#Accurate ipv4 regex
print(re.findall(r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$','255.225.215.205'))
# O/P []

# Trying email address regex
print(re.findall('^[a-z0-9_.]{1,10}[0-9]+@[^!@#$%^&*()_+][a-z]{1,10}.[a-z]{1,3}$','joyd_3e.ep560@gmail.com'))
#Explanation 
# - '^[a-z0-9_.]{1,10}[0-9]*' - Starts with (any character / number and allowed spl. chars are _ and . ) repeats 1 or more times
# - has an '@' as seprator
# - [^!@#$%^&*()_+] does not contain these spl chars
# - has a domain name of len 1 - 10 alpha
# - has a . as seprator
# - ends with ($) a domain ext of len 1 - 3 alpha
