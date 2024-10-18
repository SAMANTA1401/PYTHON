# In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation 

# Fn = Fn-1 + Fn-2
# With seed values 

# F0 = 0 and F1 = 1.

# def Fibonacci(n):
#     if n<=0:
#         print("incorrect input")
#     elif n==1:
#         return 0
#     elif n==2:
#         return 1
#     else:
#         return Fibonacci(n-1)+Fibonacci(n-2)
    

# print(Fibonacci(3))


# def Fibo_list(n):
#     fib_list = []
#     for m in range(1,n+1):
       
#         def Fibonacci(m):
#             if m<=0:
#                 print("incorrect input")
#             elif m==1:
#                 return 0
#             elif m==2:
#                 return 1
#             else:
#                 return Fibonacci(m-1)+Fibonacci(m-2)
        
#         Fibonacci(m)
#         fib_list.append(Fibonacci(m))
#     return fib_list
        
  
# print(Fibo_list(10))

# A number is Fibonacci if and only if one or both of (5*n2 + 4) or 
# (5*n2 – 4) is a perfect square

import math

def isPerfectSqure(x):
    s = int(math.sqrt(x))
    return s*s == x

def isFibonaxxi(n):
    return isPerfectSqure(5*n*n + 4) or isPerfectSqure(5*n*n - 4)

for i in range(1,11):
    if (isFibonaxxi(i) == True):
        print(i, "is a Fibonaxci number")
    else:
        print(i, "is a not a fibonnacci number")

isFibonaxxi(8)