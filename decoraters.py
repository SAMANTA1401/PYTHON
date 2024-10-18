def inc(x):
    return x+1

def dec(x):
    return x-1
# higher order function
def operate(func,x):
    result = func(x)
    return result

# print(operate(inc, 4))
# print(operate(dec, 4))

# function  can return another function
def is_called():
    def is_retrurned():
        print("hello")
    return is_retrurned
new = is_called()
# new()
# print(new)

#decoratores are collable

def make_pretty(func):
    def inner():
        print("I get decorated")
        func()
    return inner

# def ordinary():
#     print("I am ordinary")

# ordinary()
# let decorate this ordinary function
# pretty = make_pretty(ordinary) 
#instead of it we can use @make_pretty just above the ordinary() function which is to be decorated 
# by decorator make_pretty
# pretty()

# make_pretty(func) is a decorator
# and ordinary() got decorated

@make_pretty
def ordinary():
    print("I am ordinary")

# ordinary()

# decorating functions with parameter

# def divide(a,b):
#     return a/b

# divide(4, 0)

# now make a decorator to check for this case that will cause the error

def smart_divide(func):
    def inner(a,b):
        print("I am going to divide ",a, "and", b)
        if b==0:
            print("woops! can not divide .")
            return

        return func(a, b)
    return inner

@smart_divide
def divide(a,b):
    print(a/b)

# divide(4,0)

# chain decorators in python

# function can be decorated multiple times with multiple decoratores

def star(func):
    def inner(*args, **kwargs):
        print("*" *20)
        func(*args, **kwargs)
        print("*" *20)
    return inner

def percent(func):
    def inner(*args, **kwargs):
        print("%" * 20)
        func(*args, **kwargs)
        print("%" *20)
    return inner

@star
@percent
def printer(msg):
    print(msg)

printer("hello") 

