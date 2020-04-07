try:
    print (1/0)

except ZeroDivisionError as e:
    print("Error Code:{}".format(e))
    #'e' gives a nice error message

finally:
	print('finally block')