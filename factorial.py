# def factorial(n):
#     if n==0:
#         return 1
#     elif n==1:
#         return 1
#     else:
#         return (n*factorial(n-1))
# n= int(input("enter the number: "))
# print(factorial(n))


# or

def factorial(n):
    fact=1
    for i in range(1, n+1):
        fact=fact*i
    return fact
n= int(input("enter the number: "))
print(factorial(n))
