# A decorator takes in a function, adds some functionality and returns it. 
def make_pretty(func):
  print("I got decorated")
  return func   
  '''So basically we have to return from this function, but we cannot return
  Null, int, str etc. We have to return the function reference'''

@make_pretty
def ordinary():
    print("I am ordinary")

ordinary()

# O/P
# I got decorated
# I am ordinary

# if we choose to comment '# @make_pretty', then we can use alternate code
# ordinary = make_pretty(ordinary)
# ordinary()

#ex-2
#When the function that needs to be decorated has some args

def smart_divide(func): #No spl. handling needed
   def inner(a,b):
      print("I am going to divide",a,"and",b)
      print(func(a,b))  #note the ()
   return inner

@smart_divide
def divide(a,b):
    return a/b

print(divide(10,20))

# O/P
# 0.5