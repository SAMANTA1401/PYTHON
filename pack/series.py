import os
# os.getcwd()

# creating module name series.py

# n=int(input("Enter a number: "))
def factorial(n):   #function to calculate factorial
    fact =1
    for i in range(1,n+1): #range start to end-1
        fact=fact*i
    return fact

# print(factorial(3))


def fibonacci(n): #function to calculate fibonacci series
    first =0
    second =1
    print("Fibonacci series:\n",first," ",second,end='')
    # print("x")
    for i in range(1,n-1): # loop start when n=3,4,5.....
        third = second +first
        print(" ",third,end='')
        # print("y")
        first=second
        second=third
# fibonacci(3)

def exponential(x,n):
    s=0
    for i in range(n):
        print("x pow",i,"/",i,"!",end='')
        s=s+(x**i/factorial(i))
    print("\nExponential series sum:",s)

exponential(2, 3)

