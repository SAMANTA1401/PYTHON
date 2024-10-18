def factorial(n):
    fact = 1
    for i in range(1,n+1): # n==5; 1,2,3,4,5(1,n+1)
        fact = fact*i
    return fact
# print(factorial(5))

a=[1,2,3,4,5,6]

b=list(map(factorial, a))
print(b)

c=list(map(lambda x:x*x*x, a))
print(c)