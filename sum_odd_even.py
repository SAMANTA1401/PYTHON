num=int(input("enter the number: "))
sum_even=0
sum_odd=0
for i in range(num):
    if i%2==0:
        sum_even = sum_even +i
    else:
        sum_odd = sum_odd +i
print(f"sum of even number is {sum_even} and sum of odd number is {sum_odd}")
