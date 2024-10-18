# function
def add(x,y):
    sum=x+y
    return sum

print(add(4,6))

# lambda function
add2 = lambda x,y: x+y

print(add2(4, 5))

# decoraters

def first(msg):
    print(msg)

first("hello")

second = first

second("hello")