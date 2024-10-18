# take a number as argument and print number 1 to that number(argument) say 10
def nums(n):
    for i in range (1,n+1):
        # print(i)
        yield(i)

# nums(10)
# print(nums(10))

numbers = nums(10) #here nums(10) is a generator
for num in numbers:
    print(num)
    print("k")

for num in numbers:
    print(num)
    print("g")
print("jk")



