num = int(input("Enter the number: "))
prime = True
for i in range(2,num):
    if num % i==0:
        prime = False
    break
if prime:
    print("it is prime")
else:
    print("it is not a prime")