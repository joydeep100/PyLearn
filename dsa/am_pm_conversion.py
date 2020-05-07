def timeConversion(s):
	s_list = s.split(':')

	hours = int(s_list[0]) * 3600
	minutes = int(s_list[1]) * 60
	secs = int(s_list[2][:2])

	time_in_secs = hours + minutes + secs

	hours_24 = time_in_secs // 3600
	
	if 'PM' in s and hours//3600 != 12:
		hours_24+=12
	if 'AM' in s and hours//3600 == 12:
		hours_24-=12

	minutes_24 = (time_in_secs - hours ) // 60
	secs_24 = time_in_secs % 60

	return('{}:{}:{}'.format(str(hours_24).rjust(2,'0'),str(minutes_24).rjust(2,'0')\
		,str(secs_24).rjust(2,'0')))

print(timeConversion('12:45:54PM'))