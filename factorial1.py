num = int(input("Enter the number: "))
fact = 1
k = 1
if num ==0:
    print(fact)
else:
    for i in range(num):
        fact = fact * k 
        k = k+1
    print(fact)


