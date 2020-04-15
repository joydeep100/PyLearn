# A decorator takes in a function, adds some functionality and returns it. 
def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

# @make_pretty
def ordinary():
    print("I am ordinary\n")

pretty = make_pretty(ordinary)
pretty()

# O/P
# I got decorated
# I am ordinary

# Generally, we decorate a function and reassign it as,
# ordinary = make_pretty(ordinary)

# @make_pretty
# def ordinary():
#     print("I am ordinary")
# is equivalent to

# def ordinary():
#     print("I am ordinary")
# ordinary = make_pretty(ordinary)

# So we can uncomment #8, and at the end call the ordinary()

#When the function that needs to be decorated has some args

def smart_divide(func): #No spl. handling needed
   def inner(a,b):
      print("I am going to divide",a,"and",b)
      return func(a,b)
   return inner

@smart_divide
def divide(a,b):
    return a/b

print(divide(10,20))

# O/P
# 0.5