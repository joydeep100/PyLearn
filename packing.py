n = int(input())

student_marks = {}
for _ in range(n):
    name, *line = input().split()	#if input is ['joydeep',10,20,30], packs the marks in line variable
    scores = list(map(float, line))	#makes all marks of type flot
    student_marks[name] = scores
query_name = input()

sum = 0
for i in student_marks[query_name]:
    sum+=i

avg=sum/3
print('%.2f'%avg)	#printing 2 decimal points, note that no , is present
