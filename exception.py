try:
    print (1/0)

except ZeroDivisionError as e:
    print("Error Code:{}".format(e))
    #'e' gives a nice error message

    #except Exception as e:
    #When you are not sure of the exception to occur/ want to include multiple exceptions
    #As `Exception` is the class for all exceptions derived from BaseException

    #Another way for multiple exceptions
    #except (ZeroDivisionError, ValueError) as e:

finally:
	print('finally block')