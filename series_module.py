import os
# os.getcwd()

# creating module name series.py

# n=int(input("Enter a number: "))
def factorial(n):   #function to calculate factorial
    fact =1
    for i in range(1,n+1):
        fact=fact*i
    return fact

# print(factorial(n))

def fibonacci(n): #function to calculate fibonacci series
    first =0
    second =1
    print("Fibonacci series:\n",first," ",second,end='')
    for i in range(1,n-1):
        third = second +first
        print(" ",third,end='')
        first=second
        second=third
# print(fibonacci(n))

def exponential(x,n):
    s=0
    for i in range(n):
        print("x pow",i,"/",i,"!",end='')
        s=s+(x**i/factorial(i))
    print("\nExponential series sum:",s)

# print(exponential(2, 3))

