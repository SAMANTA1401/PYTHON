# def example(a,b,c):
#     avg=(a+b+c)/3
#     return avg
# result=example(2, 3, 4)
# print(result)

# multiple values return

# def example(a,b,c):
#     sum= a+b+c
#     avg = sum/3
#     return sum,avg

# result1,result2=example(2,3,5)
# print(result1)
# print(result2)

def first(a,b):
    sum=a+b
    return sum

def secong(a,b):
    avg=a/b
    return avg

value1=float(input("Enter the first input:"))
value2=float(input("enter the input:"))
result1= first(value1, value2)
result2=secong(result1, 2)
print(result2)
print(secong(10, 2))
