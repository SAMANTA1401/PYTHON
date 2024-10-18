nterm = int(input("How many terms ?"))
# current = 0
# previous = 1
# next=0
# count = 0
# if nterm==1:
#         print(0)
# else:
#     while count<nterm:
#         print(next)
#         current = next
#         next = current + previous
#         previous =current
#         count +=1

for i in range(nterm):
    if i==0:
        print("0")
        first = 0
    elif i==1:
        print("1")
        second = 1
    else:
        next = first + second
        first = second
        second = next
        print(next)



