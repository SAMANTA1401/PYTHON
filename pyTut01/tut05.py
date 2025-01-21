"""Global scop local """
"""
l = 10 #global variable

def function1(n):
    # l=5 #local variable
    global l
    l = l + 45
    m = 6
    print(l,m)
    print(n, "I have printed")

function1("this is me")
print(l)
# print(m)
"""
"""
x = 89
def harry():
    x = 20
    print(x)
    def rohan():
        # global x
        # x = 98
        print(x)
    print("before calling rohan()", x)
    rohan()
    print("after calling rohan()", x)
print(x)
harry()
print(x)
"""
"""recursive recursion vs iterative"""


# def print2(str1):
#     print2(str1)
#     print("this is " + str1)
#
# print2("harry")

"""iterative method"""

def factorial(n):
    """
    :param n: Integer
    :return: n*n-1*n-2*n-3*n-4*n-5.....
    n! = n*(n-1)!
    4! = 4*3*2*1
    """
    fac = 1
    # i = 0
    for i in range(n):
        fac = fac * (i + 1)
        # i += 1
        # print(fac)
    return fac


# number = int(input("Enter the number: "))
# print(factorial(number))


"""recursive method"""

def factorial1(n):
    if n==1:
        return 1
    else:
        return n * factorial1(n-1)


# number = int(input("Enter the number: "))
# print(factorial1(number))

"""fibbonacci series: 0 1 1 2 3 5 8 13 ...."""

def fibonacci(n):

    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

number = int(input("Enter the n'th number: "))
print(fibonacci(number))

