def add(n):
    sum=0
    for i in n:
        sum = sum +i
    return sum
def display(l,func):
    print("Addition of elements:",func(l))

display([1,2,3,4,5],add)  #function display() calling function add()

